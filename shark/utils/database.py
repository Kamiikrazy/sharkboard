from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config as cf

# check if a database host is defined
if cf("DB_URL"):
    DB_URL = cf("DB_URL")
else:  # if not, try to connect to docker container database
    DB_URL = f"postgresql://{cf('POSTGRES_USER')}:{cf('POSTGRES_PASSWORD')}@{cf('POSTGRES_HOST')}:{cf('POSTGRES_PORT')}/{cf('POSTGRES_DB')}"

engine = create_engine(DB_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
