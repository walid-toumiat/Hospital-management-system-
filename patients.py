
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from Hospital_database import get_db_connection
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(title="Hospital Management System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # يسمح لأي ملف بالاتصال
    allow_methods=["*"],
    allow_headers=["*"],
)


class Sick(BaseModel):
    name: str = Field(..., example="Ahmed")
    illness: str = Field(..., example="Flu")
    room: int = Field(..., example=101)

@app.get('/')
def home():
    return {"message": "Hospital API is running"}

@app.get('/sicklist')
def get_patients():
    conn = get_db_connection()
    rows = conn.execute('SELECT * FROM patients').fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.post('/sicklist')
def add_patient(patient: Sick):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO patients (name, illness, room) VALUES (?, ?, ?)',
        (patient.name, patient.illness, patient.room)
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return {"id": new_id, **patient.model_dump()}

@app.put('/sicklist/{sick_id}')
def update_patient(sick_id: int, patient: Sick):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE patients SET name = ?, illness = ?, room = ? WHERE id = ?',
        (patient.name, patient.illness, patient.room, sick_id)
    )
    conn.commit()
    updated = cursor.rowcount
    conn.close()
    
    if updated == 0:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {"status": "success", "id": sick_id}

@app.delete('/sicklist/{sick_id}')
def delete_patient(sick_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM patients WHERE id = ?', (sick_id,))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()

    if deleted == 0:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {"message": "Deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
