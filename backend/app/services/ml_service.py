import joblib
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent / "ml"
MODELS_DIR = BASE_DIR / "models"
CATEGORY_MODEL_PATH = MODELS_DIR / "category_classifier.joblib"
PRIORITY_MODEL_PATH = MODELS_DIR / "priority_classifier.joblib"
METADATA_PATH = BASE_DIR / "model_metadata.json"

category_model = None
priority_model = None

def load_models():
    global category_model, priority_model
    if not CATEGORY_MODEL_PATH.exists() or not PRIORITY_MODEL_PATH.exists():
        raise FileNotFoundError("Los modelos no existen. Por favor ejecuta 'python app/ml/train_model.py' primero.")
    
    if category_model is None:
        category_model = joblib.load(CATEGORY_MODEL_PATH)
    if priority_model is None:
        priority_model = joblib.load(PRIORITY_MODEL_PATH)

def predict_category(description: str) -> str:
    if category_model is None:
        load_models()
    return category_model.predict([description])[0]

def predict_priority(description: str) -> str:
    if priority_model is None:
        load_models()
    return priority_model.predict([description])[0]

def get_model_metadata() -> dict:
    if not METADATA_PATH.exists():
        raise FileNotFoundError("El archivo de metadatos no existe. Ejecuta el entrenamiento primero.")
    with open(METADATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def get_status() -> dict:
    return {
        "models_available": CATEGORY_MODEL_PATH.exists() and PRIORITY_MODEL_PATH.exists(),
        "category_model": CATEGORY_MODEL_PATH.exists(),
        "priority_model": PRIORITY_MODEL_PATH.exists(),
        "metadata_available": METADATA_PATH.exists()
    }
