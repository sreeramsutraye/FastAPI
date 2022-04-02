from fastapi import FastAPI, HTTPException, Request, status, Form, Header
from pydantic import BaseModel, Field
from request_body import Book
from uuid import UUID
from typing import Optional

#initiating FastAPI object
app = FastAPI()

  
BOOKS=[]

#decorator with [get or put or post or delete method] with root
@app.get('/')
async def get_all_books():
    if len(BOOKS)<1:
        adding_default_books()
    return BOOKS

#We are using Form for getting user login
@app.post('/books/login')
async def book_login(username: str = Form(...), password: str = Form(...)):
    return {"usermame": username, "password": password}


#You will get 201 status code when something new is created
@app.post('/', status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    BOOKS.append(book)
    
@app.get('/books/{book_id}')
async def get_book_by_id(book_id:UUID):
    for book in BOOKS:
        if book_id==book.id:
            return book
    raise raise_when_items_not_found()

@app.put('/books/{book_id}')
async def update_book(book_id:UUID, book:Book):
    counter = 0
    for book in BOOKS:
        counter+=1
        if book.id == book_id:
            BOOKS[counter - 1] = book
            return BOOKS[counter - 1]
    raise raise_when_items_not_found()
        
@app.delete('/books/{book_id}')
async def delete_book(book_id:UUID):
    counter = 0
    for book in BOOKS:
        counter += 1
        if book.id == book_id:
            del BOOKS[counter - 1]
            return "DELETED"
    raise raise_when_items_not_found()
    
        
def adding_default_books():
    book_1 = Book(
            id="6bedb5b4-ed8c-4aa8-877c-f6e0745e0849",
            title="The Psychology of Money",
            author="Morgan hosell",
            description="Great book on Personal Finanace",
            rating=5
            )
    book_2 = Book(
            id="91c868fb-19e5-4a59-aa6e-b16ad236bce9",
            title="The Fault in our Stars",
            author="John Green",
            description="A Teenage Love Story with Great Message for life",
            rating=5
            )
    book_3 = Book(
            id="c3ef14ba-b6d1-40cc-a2b8-bc531b24c96b",
            title="Do Epic Shit",
            author="Ankur Warikoo",
            description="A Short Description of all the famous books ever written",
            rating=5
            )
    book_4 = Book(
            id="8afe7d0a-8228-4917-9869-493ed9c1dbeb",
            title="The Alchemist",
            author="Paulo Ceolho",
            description="A Short and Lean Book telling story of a boy who believed in Faith",
            rating=4
            )
    book_5 = Book(
            id="a41badd9-2ab7-47f6-8831-c0025cbdf4c7",
            title="Think Like A Monk",
            author="Jay Shetty",
            description="A Great Book Saying Great Things, but this book is not for everyone",
            rating=3
            )
    
    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
    BOOKS.append(book_4)
    BOOKS.append(book_5)

#This function is used to raise an exception when the book is not found in the database
def raise_when_items_not_found():
    return HTTPException(status_code=404, 
                        detail="Book Not Found",
                        headers={"X-Header_Error":"Nothing to be seen at the UUID"})