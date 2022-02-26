from fastapi import FastAPI

app = FastAPI()


@app.get("/books/{book_id}")
async def retrieve_books(book_id):
    return {"id": book_id}