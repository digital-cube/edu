import sqlalchemy
from sqlalchemy import create_engine


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
from sequencer import seq

SqlAlchemyDeclarativeBase = declarative_base()

# engine = create_engine('sqlite:///mydb.db')
engine = create_engine('sqlite:///:memory:')

Session = sessionmaker(bind=engine)

session = Session()

class ErrorAddingCommentException(BaseException):
    pass
class ErrorEditingCommentException(BaseException):
    pass
class CommentDoesntExist(BaseException):
    pass

class User(SqlAlchemyDeclarativeBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    username = sqlalchemy.Column(sqlalchemy.String, unique=True)
    fname = sqlalchemy.Column(sqlalchemy.String)
    lname = sqlalchemy.Column(sqlalchemy.String)
    password = sqlalchemy.Column(sqlalchemy.String)

    # posts = sqlalchemy.orm.relationship('Post', back_populates='posts', lazy="joined")

    posts = sqlalchemy.orm.relationship('Post',foreign_keys='Post.id_author')

    def __init__(self, id, username, password, fname, lname):
        self.id = id
        self.username = username
        self.password = password
        self.fname = fname
        self.lname = lname


post2tag = sqlalchemy.Table('post2tag', SqlAlchemyDeclarativeBase.metadata,
    sqlalchemy.Column('id_post', sqlalchemy.String, sqlalchemy.ForeignKey('posts.id'), index=True),
    sqlalchemy.Column('id_tag', sqlalchemy.String, sqlalchemy.ForeignKey('tags.id'), index=True)

)

# guest2comment = sqlalchemy.Table('guest2comment', SqlAlchemyDeclarativeBase.metadata,
#     sqlalchemy.Column('id_guest', sqlalchemy.String, sqlalchemy.ForeignKey('guests.id'), index=True),
#     sqlalchemy.Column('id_comment', sqlalchemy.String, sqlalchemy.ForeignKey('comments.id'), index=True)
#
# )


import socket


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 0))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP



class Guest(SqlAlchemyDeclarativeBase):
    __tablename__ = 'guests'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    ip = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True)
    fname = sqlalchemy.Column(sqlalchemy.String)
    lname = sqlalchemy.Column(sqlalchemy.String)


    def __init__(self, id, email, fname, lname):
        self.id = id
        self.ip = get_ip()
        self.email = email
        self.fname = fname
        self.lname = lname

class Comment(SqlAlchemyDeclarativeBase):
    __tablename__ = 'comments'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    id_author = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('users.id'), index=True, nullable=True)
    id_guest = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('guests.id'), index=True, nullable=True)
    id_post = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('posts.id'), index=True)
    comment_text = sqlalchemy.Column(sqlalchemy.String)
    created = sqlalchemy.Column(sqlalchemy.DateTime)
    status = sqlalchemy.Column(sqlalchemy.Boolean, default=False)

    post = sqlalchemy.orm.relationship('Post',
                                       backref=sqlalchemy.orm.backref('posts'))
    # author = sqlalchemy.orm.relation('User',backref=sqlalchemy.orm.backref('users'))
    # guest = sqlalchemy.orm.relation('Guest',backref=sqlalchemy.orm.backref('guests'))
    def __init__(self, id, author, guest, post, comment_text, status):

        self.id = id
        self.author = author
        self.guest = guest
        self.post = post
        self.comment_text = comment_text
        self.status = status

        self.created = datetime.datetime.now()


class Post(SqlAlchemyDeclarativeBase):
    __tablename__ = 'posts'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    id_author = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('users.id'), index=True)
    slug = sqlalchemy.Column(sqlalchemy.String, unique=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    content = sqlalchemy.Column(sqlalchemy.Text)
    posted = sqlalchemy.Column(sqlalchemy.DateTime, index=True)
    author = sqlalchemy.orm.relationship('User', backref=sqlalchemy.orm.backref('users'))

    # def mk_slug_from_title(self):
    #     pass
    #
    # def check_slug(self, slug):
    #     pass

    tags =  sqlalchemy.orm.relationship('Tag', secondary=post2tag, backref='Post')

    comments = sqlalchemy.orm.relationship('Comment',
                                        foreign_keys='Comment.id_post')

    def add_tag(self, tag):

        self.tags.append(tag)

    def add_comment(self, author, guest, text, status):


        comment = Comment(
            seq('comments'),
            author,
            guest,
            self,
            text,
            status
        )
        try:
            session.add(comment)
            session.commit()
        except:
            session.rollback()
            raise ErrorAddingCommentException

        return True


    def __init__(self, id, author, slug, title, content):

        self.id = id
        self.author = author
        self.slug = slug
        self.title = title
        self.content = content
        self.posted = datetime.datetime.now()



class Tag(SqlAlchemyDeclarativeBase):

    __tablename__ = 'tags'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String, unique=True)

    posts =  sqlalchemy.orm.relationship('Post', secondary=post2tag, backref='Tag')

    @staticmethod
    def fix_tag_name(tag_name):
        tag_name = tag_name.strip().lower()
        tag_name = tag_name.replace('!','')
        return tag_name

    def __init__(self, id, tag_name):

        self.id = id
        self.name = Tag.fix_tag_name(tag_name)

SqlAlchemyDeclarativeBase.metadata.create_all(engine)
