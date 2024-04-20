from fastapi import APIRouter, HTTPException
from schema.patient import Patient, PatientCreate, patients, PatientUpdate

patient_router = APIRouter()

# create a new patient
@patient_router.post('/', status_code=201)
def create_patient(payload: PatientCreate):
    id_patient = len(patients) + 1
    # new_patient = Patient(id_patient, **payload)
    if len(payload.phone) > 11 or  len(payload.phone) < 11:
         return {'error': 'Invalid Phone Number'}
        
    new_patient = Patient(
        id=id_patient,
        name=payload.name,
        age=payload.age,
        sex=payload.sex,
        weight=payload.weight,
        height=payload.height,
        phone=payload.phone 

    )

    patients[id_patient] = new_patient

    return {'message': 'patient created successfully', 'data': new_patient}

# fetch all the patient 
@patient_router.get('/')
def get_all_patient():
    return {'message':'All Patient Retrieved', 'data':patients}

    
# update a patient profile
@patient_router.put('/{patient_id}', status_code=200)
def update_patient(patient_id: int, payload: PatientUpdate):
    current_patient = None
    print("11111111111111111111111111111")
    # fetch the particular patient you want ot update
    # check if the id of the fetched patient is equal to the one we passed
    # then store the fetch patient into the variable current_patient

    for key, pat in patients.items():
        print(pat.id)
        print(patient_id)
        if pat.id == patient_id:
            current_patient = pat
            break
    if not current_patient:
            raise HTTPException(status_code=404, detail="Patient not found")
    print("5555555555555555555555")

    if payload.name != None:
        current_patient.name = payload.name
    if payload.age != None:
         current_patient.age = payload.age
    if payload.sex != None:
        current_patient.sex = payload.sex
    if payload.weight != None:
        current_patient.weight = payload.weight
    if payload.height != None:
        current_patient.height = payload.height
    if payload.phone != None:
         current_patient.phone = payload.phone

    return {'message':'Patient Successfully Updated', 'data':current_patient}
    
# to delete a patient
@patient_router.delete('/{patient_id}')
def delete_patient(patient_id: int):
     patient = patients.get(patient_id)
     if not patient:
            return {"error" : "Patient not found"}
     del patients[patient_id]
     return {"message":"patient deleted successfully"}
         
     
    

    