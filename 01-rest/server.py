from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="TEST demo")

BOOKS: dict[int, dict] = {
    1: {"id": 1, "title": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling"},
    2: {"id": 2, "title": "The Hobbit", "author": "J.R.R. Tolkien"}
}

class BookIn(BaseModel):
    title: str
    author: str

@app.get("/books")      # Read all books
def list_books():
    return list(BOOKS.values())

@app.get("/books/{book_id}")     # Read single book
def get_book(book_id: int):
    if book_id not in BOOKS:
        raise HTTPException(status_code=404, detail="Book Not Found")
    return BOOKS.get(book_id)

@app.post("/books", status_code=201)    # Create book
def create_book(book: BookIn):
    new_id = max(BOOKS) + 1 if BOOKS else 1
    BOOKS[new_id] = {"id": new_id, **book.model_dump()}
    return BOOKS[new_id]

@app.put("/books/{book_id}")    # Update book
def update_book(book_id: int, book: BookIn):
    if book_id not in BOOKS:
        raise HTTPException(status_code=404, detail="Book Not Found")
    BOOKS[book_id] = {"id": book_id, **book.model_dump()}
    return BOOKS.get(book_id)

@app.delete("/books/{book_id}", status_code=204)     # Delete book
def delete_book(book_id: int):
    if book_id not in BOOKS:
        raise HTTPException(status_code=404, detail="Book Not found")
    del BOOKS[book_id]
