from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Boolean,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    external_id = Column(UUID(as_uuid=True), primary_key=False, default=uuid.uuid4)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False, unique=True)


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    external_id = Column(UUID(as_uuid=True), primary_key=False, default=uuid.uuid4)
    title = Column(String(255), nullable=False)
    summary = Column(Text, nullable=False)
    body = Column(Text, nullable=False)
    is_deleted = Column(Boolean, nullable=False)
