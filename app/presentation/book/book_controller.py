from decimal import Decimal

from fastapi import APIRouter, HTTPException

from app.config import (
    create_book,
    get_book,
    get_books,
    update_book,
    delete_book
)


router = APIRouter()


@router.post("/books", status_code=201)
def create_book_endpoint(request: dict):

    try:

        book = create_book.execute(
            title=request["title"],
            price=Decimal(str(request["price"]))
        )

        return {
            "id": book.id,
            "title": book.title,
            "price": str(book.price)
        }

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@router.get("/books/{book_id}")
def get_book_endpoint(book_id: str):

    book = get_book.execute(book_id)

    if book is None:

        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return {
        "id": book.id,
        "title": book.title,
        "price": str(book.price)
    }


@router.get("/books")
def get_books_endpoint():

    books = get_books.execute()

    return [
        {
            "id": book.id,
            "title": book.title,
            "price": str(book.price)
        }
        for book in books
    ]


@router.put("/books/{book_id}")
def update_book_endpoint(
    book_id: str,
    request: dict
):

    try:

        book = update_book.execute(
            book_id=book_id,
            title=request["title"],
            price=Decimal(str(request["price"]))
        )

        if book is None:

            raise HTTPException(
                status_code=404,
                detail="Book not found"
            )

        return {
            "id": book.id,
            "title": book.title,
            "price": str(book.price)
        }

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@router.delete("/books/{book_id}")
def delete_book_endpoint(book_id: str):

    deleted = delete_book.execute(book_id)

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return {
        "message": "Book deleted successfully"
    }