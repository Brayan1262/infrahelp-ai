from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.analyze import AnalyzeRequest, AnalyzeResponse
from app.services.analyze_service import analyze_ticket
from app.db.database import get_db
from app.services.history_service import HistoryService

router = APIRouter(prefix="/api", tags=["AI Analysis"])

@router.post("/analyze", response_model=AnalyzeResponse)
def analyze_endpoint(request: AnalyzeRequest, db: Session = Depends(get_db)):
    try:
        analysis = analyze_ticket(request.description)
        HistoryService.save_analysis(db, analysis)
        return AnalyzeResponse(**analysis)
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error inesperado al procesar el ticket: {str(e)}")

@router.get("/recommendations/categories")
def get_categories():
    return [
        "REDES",
        "WINDOWS_SERVER",
        "IMPRESORA",
        "SOFTWARE",
        "VIDEOVIGILANCIA",
        "BASE_DE_DATOS",
        "SEGURIDAD",
        "HARDWARE",
        "CORREO",
        "SISTEMA_LENTO"
    ]
