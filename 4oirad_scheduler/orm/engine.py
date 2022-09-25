from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker  # type: ignore

from settings import database_settings

SQLALCHEMY_DATABASE_URI = database_settings.full_url_sync
SQLALCHEMY_ASYNC_DATABASE_URI = database_settings.full_url_async

async_engine = create_async_engine(SQLALCHEMY_ASYNC_DATABASE_URI)
engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

Session = sessionmaker(engine)
