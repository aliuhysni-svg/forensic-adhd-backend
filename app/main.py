from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Forensic ADHD Backend Running"}

