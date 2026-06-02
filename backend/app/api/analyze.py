from fastapi import APIRouter, HTTPException
from app.schemas.analyze import AnalyzeRequest, AnalyzeResponse
from app.services.analyze_service import analyze_ticket

router = APIRouter(prefix="/api", tags=["AI Analysis"])

@router.post("/analyze", response_model=AnalyzeResponse)
def analyze_endpoint(request: AnalyzeRequest):
    try:
        result = analyze_ticket(request.description)
        return AnalyzeResponse(**result)
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error inesperado al procesar el ticket: {str(e)}")
