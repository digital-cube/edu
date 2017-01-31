from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:', echo=False)
Base = declarative_base()

from sqlalchemy import Column, Integer, String

class User(Base):
     __tablename__ = 'users'

     id = Column(Integer, primary_key=True)
     email = Column(String, unique=True)

     def __init__(self, email):
        self.email = email

     def __repr__(self):
        return "<User(email='%s'>".format(self.email)

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
