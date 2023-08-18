import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from modules.config import Config

logger = logging.getLogger(__name__)
config: Config = Config()
engine = create_engine(url=config.DB_URL, echo=config.DB_ECHO)
session = None


def get_session():
    global session, engine
    if session:
        return session
    session = sessionmaker(bind=engine)()
    return session
