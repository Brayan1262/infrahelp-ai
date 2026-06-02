import pandas as pd
from pathlib import Path
import os

DATA_FILE_PATH = Path(__file__).parent.parent / "data" / "tickets_dataset.csv"

def load_dataset() -> pd.DataFrame:
    if not DATA_FILE_PATH.exists():
        raise FileNotFoundError(f"El archivo {DATA_FILE_PATH} no existe.")
    
    df = pd.read_csv(DATA_FILE_PATH)
    
    required_columns = ["description", "category", "priority", "possible_cause", "recommended_steps"]
    missing_columns = [col for col in required_columns if col not in df.columns]
    
    if missing_columns:
        raise ValueError(f"Faltan las siguientes columnas en el dataset: {missing_columns}")
        
    return df

def get_dataset_summary() -> dict:
    df = load_dataset()
    
    total_records = int(len(df))
    categories = df["category"].unique().tolist()
    priorities = df["priority"].unique().tolist()
    
    records_by_category = df["category"].value_counts().to_dict()
    records_by_priority = df["priority"].value_counts().to_dict()
    
    return {
        "total_records": total_records,
        "categories": categories,
        "priorities": priorities,
        "records_by_category": records_by_category,
        "records_by_priority": records_by_priority
    }
