import sqlalchemy
from sqlalchemy import create_engine


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SqlAlchemyDeclarativeBase = declarative_base()

engine = create_engine('sqlite:///mydb.db')

Session = sessionmaker(bind=engine)

session = Session()



class User(SqlAlchemyDeclarativeBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    username = sqlalchemy.Column(sqlalchemy.String, unique=True)
    fname = sqlalchemy.Column(sqlalchemy.String)
    lname = sqlalchemy.Column(sqlalchemy.String)
    password = sqlalchemy.Column(sqlalchemy.String)

    def __init__(self, id, username):
        self.id = id
        self.username = username


class Post(SqlAlchemyDeclarativeBase):
    __tablename__ = 'posts'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    id_author = sqlalchemy.Column(sqlalchemy.String, index=True)
    slug = sqlalchemy.Column(sqlalchemy.String, unique=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    content = sqlalchemy.Column(sqlalchemy.Text)

    def __init__(self, id, username):
        self.id = id
        self.username = username




SqlAlchemyDeclarativeBase.metadata.create_all(engine)
