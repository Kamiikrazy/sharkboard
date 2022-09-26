from fastapi import APIRouter, Depends, Request
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from shark.utils import models, schemas
from shark.utils.crud import get_db

router = APIRouter()

# models.Base.metadata.create_all(bind=engine)


@router.get("/testing/")
async def test(request: Request):
    return {"message": "Wow, test succesful!"}


@router.get("/test/{name}")
async def test_name(request: Request, name: str):
    return {"message": f"Wow, test succesful! {name}"}


@router.post("/book/", response_model=schemas.Book)
async def post_book(book: schemas.Book, db: AsyncSession = Depends(get_db)):
    db_book = insert(models.Book).values(
        title=book.title, rating=book.rating, author_id=book.author_id
    )
    await db.execute(db_book)
    await db.commit()
    return book


@router.get("/book/")
async def get_book(db: AsyncSession = Depends(get_db)):
    book = select(models.Book)
    result = await db.execute(book)
    curr = result.scalars().all()
    return curr


@router.post("/author/")
async def post_author(author: schemas.Author, db: AsyncSession = Depends(get_db)):
    db_author = insert(models.Author).values(name=author.name, age=author.age)
    await db.execute(db_author)
    await db.commit()
    return author


@router.get("/author/")
async def get_author(db: AsyncSession = Depends(get_db)):
    book = select(models.Author)
    result = await db.execute(book)
    curr = result.scalars().all()
    return curr
