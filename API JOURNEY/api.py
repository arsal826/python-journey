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

 #/greet → returns {"message": "Welcome to my API"}

@app.get("/greet")
def greet():
    return {"message": "Welcome to my API"}

@app.get("/age")
def age():
    return {"age": 25}

@app.get("/location")
def location():
    return {"Country": "Pakistan", "City": "Karachi"}