"""Declare models and relationships."""
import uuid
from sqlalchemy import UUID, Column, DateTime, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

from .session import engine

Base = declarative_base()


class User(Base):
    """User account."""

    __tablename__ = "user"

    id = Column(String(255), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(255))
    address = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())


def create_tables():
    """Create tables in the database."""
    Base.metadata.create_all(engine)