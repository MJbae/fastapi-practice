from odmantic import Model


class Book(Model):
    keyword: str
    publisher: str
    price: int
    image: str

    class Config:
        collection = "books"
