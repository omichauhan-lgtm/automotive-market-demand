from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
import models
from routers import auth, tenants, ingest, analytics

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="AutoSight API", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(tenants.router)
app.include_router(ingest.router)
app.include_router(analytics.router)




@app.get("/")
def read_root():
    return {"message": "Welcome to AutoSight API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
