from fastapi import APIRouter, HTTPException
from schema.appointment import Appointment, AppointmentCreate, appointments, AppointmentUpdate
from schema.doctors import doctors
# from schema.patient import patients

appointment_router = APIRouter()

@appointment_router.post('/')
def create_appointment(payload: AppointmentCreate):
    appointment_id = len(appointments) + 1
    # fetch the patient and doctor
    # then check if the doctor is available
    # if doctor is available, create appointment else
    # return error message not available

    # patient = patients.get(patient_id)
    doctor = doctors.get(payload.doctor_id)
    print(doctor)

    if doctor.avalaibility == True :
        
        new_appointment = Appointment(
        id=appointment_id,
        patient_id= payload.patient_id,
        doctor_id=payload.doctor_id,
        date=payload.date

        )
        appointments[appointment_id] = new_appointment
        return {'message':'Appointment Created Successfully', 'data':new_appointment}

    else:
        return {'message':'Doctor not available'}

# get all the appointment  
@appointment_router.get('/')
def get_all_appointment():
    return {'message':'All Appointment Successfully Retrieved', 'data':appointments}

# update the appointment
@appointment_router.put('/{appointment_id}', status_code=200)
def update_appointment(appointment_id: int, payload:AppointmentUpdate):
    current_appointment = None

    for key, appointment in appointments.items():
        if appointment.id == appointment_id:
            current_appointment = appointment
            break
    
    if not current_appointment:
        raise HTTPException(status_code=404, detail="Appointment not available")

    if payload.patient_id != None:
        current_appointment.patient_id = payload.patient_id
    if payload.doctor_id != None:
        current_appointment.doctor_id = payload.doctor_id
    if payload.date != None:
        current_appointment.date = payload.date

    return {'message': ' Appointment Successfully updated', 'data':current_appointment} 


# delete an appointment

@appointment_router.delete('/{appointment_id}')
def delete_doctor(appointment_id: int):
    appointment = appointments.get(appointment_id)

    if not appointment:
        return {'error':'Appointment Not Available'}
    
    del appointments[appointment_id]
    return {"message":"Appointment Deleted Successfully"}
    
    