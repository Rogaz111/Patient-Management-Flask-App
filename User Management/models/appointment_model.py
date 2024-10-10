from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, Time, DateTime, Boolean
from database_service import Base
from datetime import datetime


class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    doctor_id = Column(Integer, ForeignKey('doctors.id'), nullable=False)
    medical_scheme_id = Column(Integer, ForeignKey('medical_schemes.id'), nullable=True)
    has_medical_scheme = Column(Boolean, nullable=False)
    appointment_date = Column(Date, nullable=False)
    appointment_time = Column(Time, nullable=False)
    reason = Column(String(255), nullable=True)
    status = Column(String(50), nullable=False, default='scheduled')  # Default status as 'Scheduled'
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, patient_id, doctor_id, appointment_date, appointment_time, reason=None,
                 medical_scheme_id=None, has_medical_scheme=False, status='scheduled', notes=None):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.medical_scheme_id = medical_scheme_id
        self.has_medical_scheme = has_medical_scheme
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time
        self.reason = reason
        self.status = status
        self.notes = notes