# coding: utf-8
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Date,
    ForeignKey,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DB_FILENAME = 'sqlite:///lariskursi.db'

Base = declarative_base()

class Subscriber(Base):
    __tablename__ = "subscriber"
    # Columns
    id = Column(Integer, primary_key=True)
    chat_id = Column(String(20), nullable=False, unique=True)


class RefCurrency(Base):
    __tablename__ = "refcurrency"

    id = Column(Integer, primary_key=True)
    code = Column(String(3))
    name = Column(String(100))
    quantity = Column(Integer)


class Rate(Base):
    __tablename__ = "rate"

    id = Column(Integer, primary_key=True)
    rate = Column(Float)
    currency_id = Column(Integer, ForeignKey('refcurrency.id'))
    date = Column(Date)


def initialize_db():
    engine = create_engine(DB_FILENAME,
                            connect_args={'check_same_thread': False})
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session


engine = create_engine(DB_FILENAME)

Base.metadata.create_all(engine)
