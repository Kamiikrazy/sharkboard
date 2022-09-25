from pydantic import BaseModel

# not done yet
class Endpoint(BaseModel):
    id: int
    name: str
    is_active: bool = True
    clicks: int

    class Config:
        orm_mode = True


# testing stuff
class Book(BaseModel):
    title: str
    rating: int
    author_id: int

    class Config:
        orm_mode = True


# testing stuff
class Author(BaseModel):
    name: str
    age: int

    class Config:
        orm_mode = True
