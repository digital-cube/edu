import sqlalchemy
from sqlalchemy import create_engine


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SqlAlchemyDeclarativeBase = declarative_base()

# engine = create_engine('sqlite:///mydb.db')
engine = create_engine('sqlite:///:memory:')

Session = sessionmaker(bind=engine)

session = Session()

class User(SqlAlchemyDeclarativeBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    username = sqlalchemy.Column(sqlalchemy.String, unique=True)
    fname = sqlalchemy.Column(sqlalchemy.String)
    lname = sqlalchemy.Column(sqlalchemy.String)
    password = sqlalchemy.Column(sqlalchemy.String)

    # posts = sqlalchemy.orm.relationship('Post', back_populates='posts')

    def __init__(self, id, username, password, fname, lname):
        self.id = id
        self.username = username
        self.password = password
        self.fname = fname
        self.lname = lname


class Post(SqlAlchemyDeclarativeBase):
    __tablename__ = 'posts'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    id_author = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('users.id'), index=True)
    slug = sqlalchemy.Column(sqlalchemy.String, unique=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    content = sqlalchemy.Column(sqlalchemy.Text)

    author = sqlalchemy.orm.relationship('User')

    # def mk_slug_from_title(self):
    #     pass
    #
    # def check_slug(self, slug):
    #     pass

    def __init__(self, id, author, slug, title, content):

        self.id = id
        self.author = author
        self.slug = slug
        self.title = title
        self.content = content


SqlAlchemyDeclarativeBase.metadata.create_all(engine)
