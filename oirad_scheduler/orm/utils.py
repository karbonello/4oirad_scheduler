import contextlib
from typing import Iterator

import sqlalchemy

from oirad_scheduler.orm.engine import SessionLocal


def get_session_web() -> Iterator[sqlalchemy.orm.Session]:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
