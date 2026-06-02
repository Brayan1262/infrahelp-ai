import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'backend')))

from backend.app.db.database import SessionLocal
from backend.app.services.history_service import HistoryService

db = SessionLocal()
analysis = {
    "description": "Prueba desde test_save",
    "predicted_category": "REDES",
    "predicted_priority": "MEDIUM",
    "possible_cause": "Prueba de causa",
    "recommended_steps": ["paso 1", "paso 2"],
    "diagnostic_message": "Prueba de diagnostico"
}

try:
    print("Guardando...")
    res = HistoryService.save_analysis(db, analysis)
    print("Guardado:", res)
    
    all_h = HistoryService.get_all_history(db)
    print("Historial:", len(all_h))
except Exception as e:
    print("Error:", e)
finally:
    db.close()
