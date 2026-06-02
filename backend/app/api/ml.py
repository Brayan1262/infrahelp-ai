from fastapi import APIRouter, HTTPException
from app.services.ml_service import get_model_metadata, get_status

router = APIRouter(prefix="/api/ml", tags=["Machine Learning"])

@router.get("/status")
def read_status():
    try:
        status = get_status()
        return status
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/metadata")
def read_metadata():
    try:
        metadata = get_model_metadata()
        return metadata
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
