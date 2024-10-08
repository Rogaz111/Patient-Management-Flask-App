from sqlalchemy import Column, Integer, String, Date, Text, LargeBinary
from database_service import Base
from datetime import date

class Patient(Base):
    #Set table name
    __tablename__ = 'patients'

    #Set Table columns
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String(10), nullable=False)  # male, female, or other
    contact_number = Column(String(15), nullable=False)
    email = Column(String(100), nullable=True)
    address = Column(Text, nullable=False)
    medical_history = Column(Text, nullable=True)
    emergency_contact_name = Column(String(100), nullable=False)
    emergency_contact_number = Column(String(15), nullable=False)
    blood_group = Column(String(3), nullable=True)  # A+, A-, B+, etc.
    photo = Column(LargeBinary, nullable=True)  # Binary data for storing image
    create_date = Column(Date, default=date.today, nullable=False)

    #Patient model getter and setters
    def __init__(self, name, date_of_birth, gender, contact_number, email, address, medical_history,
                 emergency_contact_name, emergency_contact_number, blood_group, photo=None):
        self.name = name
        self.date_of_birth = date_of_birth
        self.age = self.calculate_age()
        self.gender = gender
        self.contact_number = contact_number
        self.email = email
        self.address = address
        self.medical_history = medical_history
        self.emergency_contact_name = emergency_contact_name
        self.emergency_contact_number = emergency_contact_number
        self.blood_group = blood_group
        self.photo = photo
        self.create_date = date.today()

    def calculate_age(self):
        """Calculate age based on the date of birth."""
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return int(age)