from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import pandas as pd
import numpy as np
import os
import models, auth
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

router = APIRouter(
    prefix="/analytics",
    tags=["analytics"]
)

def get_data(tenant_id: int):
    file_path = f"data/{tenant_id}/data.csv"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="No data found. Please upload a CSV first.")
    return pd.read_csv(file_path)

@router.get("/kpis")
def get_kpis(current_user: models.User = Depends(auth.get_current_user)):
    df = get_data(current_user.tenant_id)
    
    kpis = {
        "total_customers": int(len(df)),
        "avg_income": float(df['annual_income'].mean()) if 'annual_income' in df.columns else 0,
        "avg_purchase_prob": float(df['purchase_probability'].mean()) if 'purchase_probability' in df.columns else 0,
        "top_region": df['region'].mode()[0] if 'region' in df.columns else "N/A"
    }
    return kpis

@router.get("/segments")
def get_segments(current_user: models.User = Depends(auth.get_current_user)):
    df = get_data(current_user.tenant_id)
    
    required_cols = ['age', 'annual_income', 'dealer_visit_count', 'purchase_probability']
    if not all(col in df.columns for col in required_cols):
        raise HTTPException(status_code=400, detail="Missing required columns for segmentation")
    
    # Simple K-Means
    features = df[required_cols].dropna()
    scaler = StandardScaler()
    scaled = scaler.fit_transform(features)
    
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(scaled)
    
    # Summarize clusters
    features['cluster'] = clusters
    summary = features.groupby('cluster').mean().to_dict(orient='index')
    
    return {"clusters": summary, "distribution": features['cluster'].value_counts().to_dict()}

@router.get("/forecast")
def get_forecast(current_user: models.User = Depends(auth.get_current_user)):
    df = get_data(current_user.tenant_id)
    
    if 'purchase_probability' not in df.columns or 'annual_income' not in df.columns:
         raise HTTPException(status_code=400, detail="Missing columns for forecast")
         
    # Simple regression: Income -> Purchase Prob
    X = df[['annual_income']].values
    y = df['purchase_probability'].values
    
    model = LinearRegression()
    model.fit(X, y)
    
    # Forecast for next income brackets
    future_income = np.array([[50000], [75000], [100000], [125000], [150000]])
    prediction = model.predict(future_income)
    
    return {
        "forecast": [
            {"income": int(inc[0]), "predicted_prob": float(prob)} 
            for inc, prob in zip(future_income, prediction)
        ]
    }
