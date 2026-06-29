from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is working!"}

@app.get("/greet/{name}")
def greet(name):
    return {"message": f"Hello {name}, welcome to my API!"}

@app.get("/square/{number}")
def square(number: int):
    result = number * number
    return {"number": number, "square": result}

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"a": a, "b": b, "sum": a + b}