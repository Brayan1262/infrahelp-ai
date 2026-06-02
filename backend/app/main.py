from fastapi import FastAPI

app = FastAPI(
    title="InfraHelp AI",
    description="API de IA para análisis de tickets de soporte técnico e infraestructura TI.",
    version="1.0.0"
)

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
