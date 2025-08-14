class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.available = True
        self.borrowed_by = None


class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.borrowed_books = []
