#! /usr/bin/env python
# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Subscriber(Base):
    __tablename__ = "subscriber"
    # Columns
    id = Column(Integer, primary_key=True)
    chat_id = Column(String(20), nullable=False, unique=True)
    
engine = create_engine('sqlite:///subscribers.db')

Base.metadata.create_all(engine)
