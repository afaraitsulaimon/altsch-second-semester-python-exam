from pydantic import BaseModel
from typing import Optional


# class DoctorAvaliability(Enum):
#     available = "AVAILABLE"
#     unavailable = "UNAVAILABLE"

class Doctor(BaseModel):
    id: int
    name: str
    specialization: str
    phone: str
    avalaibility: bool = True
    # avaliability: str = DoctorAvaliability.available.value


class DoctorCreate(BaseModel):
    name: str
    specialization: str
    phone: str
    avalaibility: bool = True

class DoctorUpdate(BaseModel):
    name: Optional[str] = None
    specialization: Optional[str] = None
    phone: Optional[str] = None
    avalaibility: Optional[bool] = True   

doctors = {
    1: Doctor(id=1, name="Ramat Ashraf", specialization="surgeon", phone="08032716181", avalaibility=True)
}