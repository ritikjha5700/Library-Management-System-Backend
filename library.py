# library.py
from models import Book, User

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        return book

    def add_user(self, name, email):
        user = User(name, email)
        self.users.append(user)
        return user

    def borrow_book(self, title, user_email):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                for user in self.users:
                    if user.email == user_email:
                        book.available = False
                        book.borrowed_by = user_email
                        user.borrowed_books.append(book)
                        return {"message": "Book borrowed", "title": title}
        return {"message": "Book not available or user not found"}

    def return_book(self, title, user_email):
        for book in self.books:
            if book.title.lower() == title.lower() and book.borrowed_by == user_email:
                book.available = True
                book.borrowed_by = None
                for user in self.users:
                    if user.email == user_email:
                        user.borrowed_books.remove(book)
                return {"message": "Book returned", "title": title}
        return {"message": "Book not found or not borrowed by this user"}
