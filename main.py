from fastapi import FastAPI
from routers.patient import patient_router
from routers.doctor import doctor_router
from routers.appointment import appointment_router

app = FastAPI()

app.include_router(patient_router,prefix='/patient', tags=['Patient'])
app.include_router(doctor_router,prefix='/doctor', tags=['Doctor'])
app.include_router(appointment_router,prefix='/appointment', tags=['Appointment'])

@app.get('/')
def get_home():
    return {"Home":"Hello World"}