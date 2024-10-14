from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from database_service import Base
from datetime import datetime


class ErrorLog(Base):
    __tablename__ = 'error_log'
    id = Column(Integer, primary_key=True, autoincrement=True)
    error_message = Column(Text, nullable=True)
    error_table = Column(String, nullable=True)
    error_occurred = Column(Boolean, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, error_message, error_table, error_occurred):
        self.error_message = error_message
        self.error_table = error_table
        self.error_occurred = error_occurred