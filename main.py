from enum import Enum

from fastapi import FastAPI


class BookGenre(str, Enum):
    action = "action"
    sf = "science-fiction"
    romance = "love-fiction"


app = FastAPI()


@app.get("/books/{book_id}")
async def retrieve_books(book_id: int):
    return {"id": book_id}


@app.get("/genres/{genre_name}")
async def retrieve_genres(genre_name: BookGenre):
    if genre_name == BookGenre.action:
        return {"genre_name": genre_name}
    else:
        return {"genre_name": genre_name}
