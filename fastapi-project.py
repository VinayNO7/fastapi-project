from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class BookRequest(BaseModel):
    author : str
    title : str
    price : float
    isAvailable : bool

app = FastAPI()

books: List[BookRequest] = []

@app.get("/list",response_model=List[BookRequest])
def get_books():
    return books

@app.post("/create")
def add_book(book: BookRequest):
    books.append(book)
    return {"message" : "succesfully added a book"}

@app.delete("/delete")
def delete_book(title:str):
    for i in range(len(books)):
        book = books[i]
        if book.title == title:
            books.pop(i)
            return{"message" : "succesfully deleted"}
    return {"message" : "book not found"}

@app.put("/update")
def update_book(title: str, book: BookRequest):
    for i in range(len(books)):
        if books[i].title == title:
            books[i] = book
            return {"message": "update successfully"}
    return {"book cant be updated"}