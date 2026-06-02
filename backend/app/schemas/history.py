from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class TicketHistoryResponse(BaseModel):
    id: int
    description: str
    predicted_category: str
    predicted_priority: str
    possible_cause: str
    recommended_steps: List[str]
    diagnostic_message: str
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
