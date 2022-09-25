from fastapi import APIRouter, Request, Depends

from sqlalchemy.orm import Session

from shark.utils.crud import get_db
from shark.utils import models, schemas
from shark.utils.database import engine

router = APIRouter()

models.Base.metadata.create_all(bind=engine)


@router.get("/testing/")
async def test(request: Request):
    return {"message": "Wow, test succesful!"}


@router.get("/test/{name}")
async def test_name(request: Request, name: str):
    return {"message": f"Wow, test succesful! {name}"}


@router.post("/book/", response_model=schemas.Book)
async def post_book(book: schemas.Book, db: Session = Depends(get_db)):
    db_book = models.Book(
        title=book.title, rating=book.rating, author_id=book.author_id
    )
    db.add(db_book)
    db.commit()
    return db_book


@router.get("/book/")
async def get_book(db: Session = Depends(get_db)):
    book = db.query(models.Book).all()
    return book


@router.post("/author/", response_model=schemas.Author)
async def post_author(author: schemas.Author, db: Session = Depends(get_db)):
    db_author = models.Author(name=author.name, age=author.age)
    db.add(db_author)
    db.commit()
    return db_author


@router.get("/author/")
async def get_author(db: Session = Depends(get_db)):
    author = db.query(models.Author).all()
    return author
