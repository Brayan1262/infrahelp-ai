from pydantic import BaseModel, Field
from typing import List

class AnalyzeRequest(BaseModel):
    description: str = Field(..., min_length=10, max_length=1000, description="Descripción del ticket de soporte")

class AnalyzeResponse(BaseModel):
    description: str
    predicted_category: str
    predicted_priority: str
    possible_cause: str
    recommended_steps: List[str]
    diagnostic_message: str
