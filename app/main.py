from fastapi import FastAPI

from app.presentation.book.book_controller import router as book_router


app = FastAPI()

app.include_router(book_router)


@app.get("/")
def home():

    return {
        "message": "Bookstore API is running"
    }