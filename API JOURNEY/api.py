from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Arsal, your first API is working!"}
@app.get("/about")
def about():
    return {"name": "Arsal", "role": "Backend Developer", "learning": "FastAPI"}

@app.get("/skills")
def skills():
    return {"skills": ["Python", "Dictionaries", "File Handling", "FastAPI"]}