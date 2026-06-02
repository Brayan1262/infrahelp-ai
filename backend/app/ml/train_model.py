import os
import json
import joblib
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

# Rutas
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR.parent / "data" / "tickets_dataset.csv"
MODELS_DIR = BASE_DIR / "models"
MODELS_DIR.mkdir(parents=True, exist_ok=True)

CATEGORY_MODEL_PATH = MODELS_DIR / "category_classifier.joblib"
PRIORITY_MODEL_PATH = MODELS_DIR / "priority_classifier.joblib"
METADATA_PATH = BASE_DIR / "model_metadata.json"

def train():
    print(f"Cargando dataset desde {DATA_PATH}...")
    df = pd.read_csv(DATA_PATH)
    
    X = df["description"]
    y_category = df["category"]
    y_priority = df["priority"]

    # --- CATEGORY MODEL ---
    print("Entrenando modelo de Categoría...")
    X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(
        X, y_category, test_size=0.2, random_state=42, stratify=y_category
    )
    
    category_pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(lowercase=True, ngram_range=(1, 2), max_features=5000)),
        ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced"))
    ])
    
    category_pipeline.fit(X_train_c, y_train_c)
    y_pred_c = category_pipeline.predict(X_test_c)
    acc_c = accuracy_score(y_test_c, y_pred_c)
    print(f"Accuracy de Categoría: {acc_c:.4f}")
    
    # --- PRIORITY MODEL ---
    print("Entrenando modelo de Prioridad...")
    X_train_p, X_test_p, y_train_p, y_test_p = train_test_split(
        X, y_priority, test_size=0.2, random_state=42, stratify=y_priority
    )
    
    priority_pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(lowercase=True, ngram_range=(1, 2), max_features=5000)),
        ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced"))
    ])
    
    priority_pipeline.fit(X_train_p, y_train_p)
    y_pred_p = priority_pipeline.predict(X_test_p)
    acc_p = accuracy_score(y_test_p, y_pred_p)
    print(f"Accuracy de Prioridad: {acc_p:.4f}")
    
    # Guardar Modelos
    joblib.dump(category_pipeline, CATEGORY_MODEL_PATH)
    joblib.dump(priority_pipeline, PRIORITY_MODEL_PATH)
    
    # Guardar Metadata
    metadata = {
        "project": "InfraHelp AI",
        "model_type": "TF-IDF + Logistic Regression",
        "trained_models": [
            "category_classifier.joblib",
            "priority_classifier.joblib"
        ],
        "total_records": len(df),
        "category_accuracy": float(acc_c),
        "priority_accuracy": float(acc_p),
        "categories": y_category.unique().tolist(),
        "priorities": y_priority.unique().tolist()
    }
    
    with open(METADATA_PATH, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
        
    print(f"\nModelos guardados exitosamente en {MODELS_DIR}")
    print(f"Metadatos guardados en {METADATA_PATH}")

if __name__ == "__main__":
    train()
