from sqlalchemy import Column, Integer, String, Date, Text, Float
from database_service import Base
from datetime import date


class MedicalScheme(Base):
    __tablename__ = 'medical_schemes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    scheme_name = Column(String(100), nullable=False)
    scheme_code = Column(String(100), nullable=False)
    scheme_administrator = Column(String(100), nullable=False)
    scheme_contact_number = Column(String(15), nullable=False)
    scheme_email = Column(String(100), nullable=False)
    scheme_address = Column(Text, nullable=False)
    scheme_premium = Column(Float, nullable=False)
    scheme_status = Column(String(100), nullable=False)
    create_date = Column(Date, default=date.today, nullable=False)

    def __init__(self, scheme_name, scheme_code, scheme_administrator, scheme_contact_number, scheme_email,
                 scheme_address,
                 scheme_premium, scheme_status):
        self.scheme_name = scheme_name
        self.scheme_code = scheme_code
        self.scheme_administrator = scheme_administrator
        self.scheme_contact_number = scheme_contact_number
        self.scheme_email = scheme_email
        self.scheme_address = scheme_address
        self.scheme_premium = scheme_premium
        self.scheme_status = scheme_status
