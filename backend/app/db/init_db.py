from app.db.database import Base, engine
from app.models.ticket_history import TicketHistory

def init_db():
    Base.metadata.create_all(bind=engine)
