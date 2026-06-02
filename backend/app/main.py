from fastapi import FastAPI
from app.api.dataset import router as dataset_router
from app.api.ml import router as ml_router
from app.api.analyze import router as analyze_router

app = FastAPI(
    title="InfraHelp AI",
    description="API de IA para análisis de tickets de soporte técnico e infraestructura TI.",
    version="1.0.0"
)

app.include_router(dataset_router)
app.include_router(ml_router)
app.include_router(analyze_router)

@app.get("/")
def read_root():
    return {
        "message": "InfraHelp AI funcionando correctamente",
        "status": "ok",
        "version": "1.0.0"
    }

@app.get("/api/health")
def health_check():
    return {
        "service": "InfraHelp AI",
        "status": "healthy"
    }
