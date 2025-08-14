# main.py
from fastapi import FastAPI
from library import Library
from schemas import BookCreate, UserCreate, BorrowRequest, ReturnRequest

app = FastAPI()
library = Library()

@app.get("/")
def home():
    return {"message": "Welcome to Library API"}

@app.get("/books")
def get_all_books():
    return {"books": library.books}

@app.get("/books/{book_id}")
def get_book(book_id: int):
    if 0 <= book_id < len(library.books):
        return library.books[book_id]
    return{"error": "Book not found"}

@app.post("/books/")
def add_book(book: BookCreate):
    return library.add_book(book.title, book.author)

@app.post("/users/")
def add_user(user: UserCreate):
    return library.add_user(user.name, user.email)

@app.post("/borrow/")
def borrow_book(req: BorrowRequest):
    return library.borrow_book(req.title, req.user_email)

@app.post("/return/")
def return_book(req: ReturnRequest):
    return library.return_book(req.title, req.user_email)
