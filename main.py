from enum import Enum
from typing import Optional

from fastapi import FastAPI


class BookGenre(str, Enum):
    action = "action"
    sf = "science-fiction"
    romance = "love-fiction"


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
