from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str

class UserCreate(BaseModel):
    name: str
    email: str

class BorrowRequest(BaseModel):
    title: str
    user_email: str

class ReturnRequest(BaseModel):
    title: str
    user_email: str
