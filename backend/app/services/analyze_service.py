from app.services.ml_service import predict_category, predict_priority
from app.services.recommendation_service import get_recommendation

def analyze_ticket(description: str) -> dict:
    try:
        category = predict_category(description)
        priority = predict_priority(description)
    except FileNotFoundError:
        raise FileNotFoundError("Los modelos de IA no están entrenados. Ejecuta python app/ml/train_model.py")
    
    recommendation = get_recommendation(category, description)
    possible_cause = recommendation["possible_cause"]
    recommended_steps = recommendation["recommended_steps"]
        
    diagnostic_message = f"El ticket fue clasificado como {category} con prioridad {priority}. Se recomienda iniciar la revisión siguiendo los pasos técnicos sugeridos y documentar la solución aplicada."
    
    return {
        "description": description,
        "predicted_category": category,
        "predicted_priority": priority,
        "possible_cause": possible_cause,
        "recommended_steps": recommended_steps,
        "diagnostic_message": diagnostic_message
    }
