"""
Main module for work with database
"""
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# TODO: use some library to load config. Not pure import
from modules.config import Config  # pylint: disable=no-name-in-module,import-error

logger = logging.getLogger(__name__)
config: Config = Config()
engine = create_engine(url=config.DB_URL, echo=config.DB_ECHO)
session = None  # pylint: disable=invalid-name


def get_session():
    """
    Get sql alchemy session
    """
    # TODO: why we use global here?
    global session, engine  # pylint: disable=global-variable-not-assigned
    if session:
        return session
    session = sessionmaker(bind=engine)()
    return session
