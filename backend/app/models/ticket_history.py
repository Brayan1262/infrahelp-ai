from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.db.database import Base

class TicketHistory(Base):
    __tablename__ = "ticket_history"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(1000), nullable=False)
    predicted_category = Column(String(100), nullable=False)
    predicted_priority = Column(String(50), nullable=False)
    possible_cause = Column(String(500), nullable=False)
    recommended_steps = Column(Text, nullable=False)
    diagnostic_message = Column(String(1000), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
