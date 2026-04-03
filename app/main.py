from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
import uuid

app = FastAPI()

origins = [
    "https://floarko.fi",
    "https://www.floarko.fi",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Forensic ADHD Backend Running"}

@app.get("/create-session")
def create_session():
    session_id = str(uuid.uuid4())
    access_code = str(random.randint(10000000, 99999999))

    return {
        "session_id": session_id,
        "access_code": access_code,
        "status": "created"
    }
