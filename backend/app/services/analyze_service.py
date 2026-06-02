import random
from app.services.ml_service import predict_category, predict_priority
from app.services.dataset_service import load_dataset

def analyze_ticket(description: str) -> dict:
    try:
        category = predict_category(description)
        priority = predict_priority(description)
    except FileNotFoundError:
        raise FileNotFoundError("Los modelos de IA no están entrenados. Ejecuta python app/ml/train_model.py")
    
    df = load_dataset()
    df_similar = df[df["category"] == category]
    
    if not df_similar.empty:
        sample_ticket = df_similar.sample(1).iloc[0]
        possible_cause = sample_ticket["possible_cause"]
        steps_str = sample_ticket["recommended_steps"]
        recommended_steps = [step.strip() for step in steps_str.split(";") if step.strip()]
    else:
        possible_cause = "La incidencia requiere revisión técnica para determinar la causa raíz."
        recommended_steps = ["Contactar soporte de nivel superior", "Revisar logs del sistema"]
        
    diagnostic_message = f"El ticket fue clasificado como {category} con prioridad {priority}. Se recomienda iniciar la revisión siguiendo los pasos técnicos sugeridos y documentar la solución aplicada."
    
    return {
        "description": description,
        "predicted_category": category,
        "predicted_priority": priority,
        "possible_cause": possible_cause,
        "recommended_steps": recommended_steps,
        "diagnostic_message": diagnostic_message
    }
