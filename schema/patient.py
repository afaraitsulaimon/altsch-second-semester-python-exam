from pydantic import BaseModel
from typing import Optional

class Patient(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight: int
    height: int
    phone: str

class PatientCreate(BaseModel):
    name: str
    age: int
    sex: str
    weight: int
    height: int
    phone: str

class PatientUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    sex:  Optional[str] = None
    weight: Optional[int] = None
    height: Optional[int] = None
    phone:  Optional[str] = None
    
patients = {
    1: Patient(id=1, name="Renied Jaaj", age=24, sex="Male", weight=43, height=8, phone="08032716181")
}
