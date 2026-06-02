import json
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.ticket_history import TicketHistory
from app.schemas.history import TicketHistoryResponse
from app.repositories.history_repository import HistoryRepository

class HistoryService:
    @staticmethod
    def save_analysis(db: Session, analysis: dict) -> TicketHistoryResponse:
        steps_json = json.dumps(analysis["recommended_steps"])
        
        ticket = TicketHistory(
            description=analysis["description"],
            predicted_category=analysis["predicted_category"],
            predicted_priority=analysis["predicted_priority"],
            possible_cause=analysis["possible_cause"],
            recommended_steps=steps_json,
            diagnostic_message=analysis["diagnostic_message"]
        )
        
        saved_ticket = HistoryRepository.create(db, ticket)
        return HistoryService.map_to_response(saved_ticket)

    @staticmethod
    def map_to_response(ticket: TicketHistory) -> TicketHistoryResponse:
        steps_list = json.loads(ticket.recommended_steps)
        return TicketHistoryResponse(
            id=ticket.id,
            description=ticket.description,
            predicted_category=ticket.predicted_category,
            predicted_priority=ticket.predicted_priority,
            possible_cause=ticket.possible_cause,
            recommended_steps=steps_list,
            diagnostic_message=ticket.diagnostic_message,
            created_at=ticket.created_at
        )

    @staticmethod
    def get_all_history(db: Session) -> list[TicketHistoryResponse]:
        tickets = HistoryRepository.find_all(db)
        return [HistoryService.map_to_response(t) for t in tickets]

    @staticmethod
    def get_history_by_id(db: Session, ticket_id: int) -> TicketHistoryResponse:
        ticket = HistoryRepository.find_by_id(db, ticket_id)
        if not ticket:
            raise HTTPException(status_code=404, detail="Ticket no encontrado")
        return HistoryService.map_to_response(ticket)

    @staticmethod
    def get_history_by_category(db: Session, category: str) -> list[TicketHistoryResponse]:
        tickets = HistoryRepository.find_by_category(db, category)
        return [HistoryService.map_to_response(t) for t in tickets]

    @staticmethod
    def get_history_by_priority(db: Session, priority: str) -> list[TicketHistoryResponse]:
        tickets = HistoryRepository.find_by_priority(db, priority)
        return [HistoryService.map_to_response(t) for t in tickets]

    @staticmethod
    def delete_history(db: Session, ticket_id: int) -> dict:
        ticket = HistoryRepository.find_by_id(db, ticket_id)
        if not ticket:
            raise HTTPException(status_code=404, detail="Ticket no encontrado")
        HistoryRepository.delete(db, ticket)
        return {"message": "Ticket eliminado del historial correctamente"}
