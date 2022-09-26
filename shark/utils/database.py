from decouple import config as cf
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# check if a database host is defined
if cf("DB_URL"):
    DB_URL = cf("DB_URL")
else:  # if not, try to connect to docker container database
    DB_URL = f"postgresql+asyncpg://{cf('POSTGRES_USER')}:{cf('POSTGRES_PASSWORD')}@{cf('POSTGRES_HOST')}:{cf('POSTGRES_PORT')}/{cf('POSTGRES_DB')}"

engine = create_async_engine(DB_URL, echo=False)
engine.begin()
SessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
Base = declarative_base()


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
