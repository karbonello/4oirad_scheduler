from typing import Optional, Iterator

import sqlalchemy

from oirad_scheduler.settings import database_settings
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import as_declarative, scoped_session, sessionmaker


ASYNC_DRIVER_NAME = "postgresql+asyncpg"


def make_async_session_factory(
    database_url: str = database_settings.full_url_async,
) -> sessionmaker:
    return sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=create_async_engine(database_url),
        class_=AsyncSession,
    )


def make_async_scoped_session_factory(
    database_url: Optional[str] = None,
) -> scoped_session:
    database_url = database_url or database_settings.full_url_async
    session_factory = make_async_session_factory(database_url)
    return scoped_session(session_factory)


AsyncScopedSession = make_async_scoped_session_factory()

metadata = MetaData()


@as_declarative(metadata=metadata)
class Base:
    pass
