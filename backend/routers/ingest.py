from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
import pandas as pd
import io
import models, auth
from database import get_db

router = APIRouter(
    prefix="/ingest",
    tags=["ingest"]
)

@router.post("/upload-csv")
async def upload_csv(
    file: UploadFile = File(...), 
    current_user: models.User = Depends(auth.get_current_user), 
    db: Session = Depends(get_db)
):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload a CSV.")
    
    # Create directory for tenant data
    import os
    data_dir = f"data/{current_user.tenant_id}"
    os.makedirs(data_dir, exist_ok=True)
    file_path = f"{data_dir}/data.csv"
    
    content = await file.read()
    with open(file_path, "wb") as f:
        f.write(content)
    
    df = pd.read_csv(io.BytesIO(content))
    
    # Process Region Data (Example) - Keep this for DB sync
    if 'region' in df.columns:
        for _, row in df.iterrows():
            region = db.query(models.Region).filter(
                models.Region.tenant_id == current_user.tenant_id,
                models.Region.name == row['region']
            ).first()
            
            if not region:
                region = models.Region(
                    tenant_id=current_user.tenant_id,
                    name=row['region'],
                    population=row.get('population', 0),
                    income_median=row.get('income_median', 0.0)
                )
                db.add(region)
            else:
                region.population = row.get('population', region.population)
                region.income_median = row.get('income_median', region.income_median)
        
        db.commit()
        return {"message": f"Successfully processed {len(df)} rows and saved for analytics", "columns": list(df.columns)}
    
    return {"message": "File uploaded", "columns": list(df.columns)}
