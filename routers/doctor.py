from fastapi import APIRouter, HTTPException
from schema.doctors import Doctor, DoctorCreate, doctors, DoctorUpdate


doctor_router = APIRouter()


# create a new doctor
@doctor_router.post('/', status_code=201)
def create_doctor(payload: DoctorCreate):
    new_doctor_id = len(doctors) + 1
    if len(payload.phone) > 11 or len(payload.phone) < 11:
         return {'error':'Phone not valid'}
        

    new_doctor = Doctor(
        id=new_doctor_id,
        name=payload.name,
        specialization=payload.specialization,
        phone=payload.phone,
        
    )

    doctors[new_doctor_id] = new_doctor

    return {'message': 'patient created successfully', 'data': new_doctor}

    
 # fetch all the doctors

@doctor_router.get('/')
def get_all_doctor():
    return {'message':'All Patient Retrieved', 'data':doctors}



   
# update a doctor profile
@doctor_router.put('/{doctor_id}', status_code=200)
def update_doctor(doctor_id: int, payload: DoctorUpdate):
    current_doctor = None
    
    for key, doctor in doctors.items():
        if doctor.id == doctor_id:
            current_doctor = doctor
            break
    if not current_doctor:
            raise HTTPException(status_code=404, detail="Doctor not found")

    if payload.name != None:
        current_doctor.name = payload.name
    if payload.specialization != None:
        current_doctor.specialization = payload.specialization
    if payload.phone != None:
        current_doctor.phone = payload.phone
    if payload.avalaibility != None:
        current_doctor.avalaibility = payload.avalaibility
    
    return {'message':'Doctor Profile Successfully Updated', 'data':current_doctor}
    

    # to delete a doctor
@doctor_router.delete('/{doctor_id}')
def delete_doctor(doctor_id: int):
     doctor = doctors.get(doctor_id)
     if not doctor:
            return {"error" : "Doctor not found"}
     del doctors[doctor_id]
     return {"message":"Doctor Profile deleted successfully"}