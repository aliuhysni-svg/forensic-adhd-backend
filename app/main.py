from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
import uuid

app = FastAPI()

# CORS (WordPress + Elementor + Floarko)
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

# In-memory storage
sessions = {}

# Health check
@app.get("/")
def root():
    return {"message": "Forensic ADHD Backend Running"}


# Create session
@app.get("/create-session")
def create_session():

    session_id = str(uuid.uuid4())
    access_code = str(random.randint(10000000, 99999999))

    sessions[access_code] = {
        "session_id": session_id,
        "access_code": access_code,
        "answers": {},
        "status": "created"
    }

    return sessions[access_code]


# Save answers
@app.post("/save-answer/{code}")
def save_answer(code: str, answers: dict):

    session = sessions.get(code)

    if not session:
        return {"error": "Session not found"}

    if "answers" not in session:
        session["answers"] = {}

    session["answers"].update(answers)

    session["status"] = "in_progress"

    return {
        "status": "saved",
        "answers": session["answers"]
    }


# Load session
@app.get("/load-session/{code}")
def load_session(code: str):

    session = sessions.get(code)

    if not session:
        return {"error": "Session not found"}

    return session


# Finish session (optional future use)
@app.post("/finish-session/{code}")
def finish_session(code: str):

    session = sessions.get(code)

    if not session:
        return {"error": "Session not found"}

    session["status"] = "completed"

    return {
        "status": "completed",
        "access_code": code
    }    }

    return {
        "session_id": session_id,
        "access_code": access_code,
        "status": "created"
    }

@app.get("/load-session/{code}")
def load_session(code: str):

    session = sessions.get(code)

    if not session:
        return {"error": "Session not found"}

    return session


@app.post("/save-answer/{code}")
def save_answer(code: str, answers: dict):

    session = sessions.get(code)

    if not session:
        return {"error": "Session not found"}

    session["answers"].update(answers)

    return {
        "status": "saved",
        "answers": session["answers"]
    }
