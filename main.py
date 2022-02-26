from fastapi import FastAPI

app = FastAPI()


@app.get("/books/{book_id}")
async def retrieve_books(book_id: int):
    return {"id": book_id}