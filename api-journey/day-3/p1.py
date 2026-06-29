from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

books = [
    {"id": 1, "title": "Python Crash Course", "author": "Eric Matthes"},
    {"id": 2, "title": "Clean Code", "author": "Robert Martin"},
]

# This describes what a new book should look like
class Book(BaseModel):
    id: int
    title: str
    author: str

@app.get("/books")
def get_books():
    return {"books": books}

@app.post("/books")
def add_book(book: Book):
    books.append(book.dict())
    return {"message": "Book added!", "book": book}

@app.get("/books/{book_id}")
def get_one_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return {"book": book}
    return {"message": "Book not found"}