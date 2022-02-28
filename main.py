from enum import Enum
from typing import Optional, List

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field


class BookGenre(str, Enum):
    action = "action"
    sf = "science-fiction"
    romance = "love-fiction"


class Book(BaseModel):
    id: int
    name: str = Field(max_length=100, description="it is not allowed to be over 100 letters in name field")
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: Optional[float] = None
    tag: List[str] = ["hello", "world"]
    genre: Optional[List[BookGenre]] = None


app = FastAPI()


@app.get("/books/")
async def list_books(
        q: Optional[str] = Query(None, min_length=1, max_length=10, regex="^fixedquery$")
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


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
