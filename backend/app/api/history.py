from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.history import TicketHistoryResponse
from app.services.history_service import HistoryService

router = APIRouter(prefix="/api/history", tags=["History"])

@router.get("", response_model=List[TicketHistoryResponse])
def get_history(db: Session = Depends(get_db)):
    return HistoryService.get_all_history(db)

@router.get("/{ticket_id}", response_model=TicketHistoryResponse)
def get_history_by_id(ticket_id: int, db: Session = Depends(get_db)):
    return HistoryService.get_history_by_id(db, ticket_id)

@router.get("/category/{category}", response_model=List[TicketHistoryResponse])
def get_history_by_category(category: str, db: Session = Depends(get_db)):
    return HistoryService.get_history_by_category(db, category)

@router.get("/priority/{priority}", response_model=List[TicketHistoryResponse])
def get_history_by_priority(priority: str, db: Session = Depends(get_db)):
    return HistoryService.get_history_by_priority(db, priority)

@router.delete("/{ticket_id}")
def delete_history(ticket_id: int, db: Session = Depends(get_db)):
    return HistoryService.delete_history(db, ticket_id)
