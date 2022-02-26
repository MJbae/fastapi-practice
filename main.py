from enum import Enum
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class BookGenre(str, Enum):
    action = "action"
    sf = "science-fiction"
    romance = "love-fiction"


class Book(BaseModel):
    id: int
    name: str
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.get("/books/{book_id}")
async def retrieve_books(book_id: int, needy: str, skp: int = 0, limit: Optional[int] = None):
    return {"id": book_id, "needy": needy, "skip": skp, "limit": limit}


@app.get("/genres/{genre_name}")
async def retrieve_genres(genre_name: BookGenre):
    if genre_name == BookGenre.action:
        return {"genre_name": genre_name}
    else:
        return {"genre_name": genre_name}


@app.post("/books/")
async def create_book(book: Book):
    return book


@app.patch("/books/{book_id}")
async def update_partially_book(book_id: int, book: Book):
    result = {**book.dict(), "id": book_id, "updated": True}
    return result
