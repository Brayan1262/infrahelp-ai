from fastapi import APIRouter, HTTPException
from app.services.dataset_service import get_dataset_summary, load_dataset

router = APIRouter(prefix="/api/dataset", tags=["Dataset"])

@router.get("/summary")
def get_summary():
    try:
        summary = get_dataset_summary()
        return summary
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/sample")
def get_sample():
    try:
        df = load_dataset()
        # Devuelve los primeros 5 registros
        sample = df.head(5).to_dict(orient="records")
        return sample
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
