from sqlalchemy.orm import Session
from app.models.ticket_history import TicketHistory

class HistoryRepository:
    @staticmethod
    def create(db: Session, ticket: TicketHistory) -> TicketHistory:
        db.add(ticket)
        db.commit()
        db.refresh(ticket)
        return ticket

    @staticmethod
    def find_all(db: Session) -> list[TicketHistory]:
        return db.query(TicketHistory).order_by(TicketHistory.created_at.desc()).all()

    @staticmethod
    def find_by_id(db: Session, ticket_id: int) -> TicketHistory | None:
        return db.query(TicketHistory).filter(TicketHistory.id == ticket_id).first()

    @staticmethod
    def find_by_category(db: Session, category: str) -> list[TicketHistory]:
        return db.query(TicketHistory).filter(TicketHistory.predicted_category == category).order_by(TicketHistory.created_at.desc()).all()

    @staticmethod
    def find_by_priority(db: Session, priority: str) -> list[TicketHistory]:
        return db.query(TicketHistory).filter(TicketHistory.predicted_priority == priority).order_by(TicketHistory.created_at.desc()).all()

    @staticmethod
    def delete(db: Session, ticket: TicketHistory) -> None:
        db.delete(ticket)
        db.commit()
