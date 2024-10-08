from sqlalchemy import Column, Integer, String, Date, Text, LargeBinary
from database_service import Base
from datetime import date


class Doctor(Base):
    __tablename__ = 'doctors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String(10), nullable=False)
    email = Column(String(100), nullable=True)
    contact_number = Column(String(15), nullable=False)
    department = Column(String(100), nullable=False)
    address = Column(Text, nullable=False)
    profile_photo = Column(LargeBinary, nullable=True)
    create_date = Column(Date, default=date.today, nullable=False)

    def __init__(self,first_name,last_name,date_of_birth,gender,email,contact_number,department,address,profile_photo=None):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.email = email
        self.contact_number = contact_number
        self.department = department
        self.address = address
        self.profile_photo = profile_photo
        self.create_date = date.today()