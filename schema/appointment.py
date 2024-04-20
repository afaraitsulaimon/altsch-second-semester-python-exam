from pydantic import BaseModel
from typing import Optional

class Appointment(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    date: str


class AppointmentCreate(BaseModel):
    patient_id: int
    doctor_id: int
    date: str

class AppointmentUpdate(BaseModel):
    patient_id: Optional[int] = None
    doctor_id: Optional[int] = None
    date: Optional[str] = None


appointments = {
    1: Appointment(id=1, patient_id=1, doctor_id = 2, date="18-02-2024")
}
