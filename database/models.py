from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Float
)

from .base import Base


class Animal(Base):
    __tablename__ = "animals"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    image_path = Column(String)


class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    price = Column(Float)
    name = Column(String)


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    date = Column(String)
    price = Column(Float)
    name = Column(String)
    mail = Column(String)
    way_get = Column(String)
    count = Column(Integer)
