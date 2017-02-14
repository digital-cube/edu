import datetime
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('sqlite:///:memory:', echo=False)
Base = declarative_base()

from sqlalchemy import Column, Integer, String, SmallInteger, Boolean, Text, DateTime, orm
from sequencer import seq



class ToManyAttemptsException(NameError):
    pass


class User(Base):
     __tablename__ = 'users'

     id = Column(String, primary_key=True)
     email = Column(String, unique=True)
     # articles = relationship('Article', foreign_keys='Article.id_author')

     def __init__(self, id, email):
        self.id = id
        self.email = email

#
# article2tag = Table('article2tag', Base.metadata,
#     Column('id_article', String, ForeignKey('articles.id'), index=True),
#     Column('id_tag', String, ForeignKey('tags.id'), index=True)
#
# )


class Article(Base):
     __tablename__ = 'articles'

     id = Column(String(10), primary_key=True)
     slug = Column(String, unique=True)
     title = Column(String, unique=False)
     id_category = Column(String, unique=False, default=None)
     id_user = Column(String, ForeignKey('users.id'), index=True)
     content = Column(String)
     number_of_likes = Column(Integer)
     number_of_comments = Column(Integer)
     # author = relationship('User', back_populates="articles")

     def __init__(self, id, slug, title, id_category, id_user, content):
         self.id = id
         self.slug = slug
         self.title = title
         self.id_user = id_user
         self.content = content
         self.id_category = id_category
         # self.number_of_likes = number_of_likes
         # self.number_of_comments = number_of_comments

     # author = orm.relationship('User', backref = orm.backref('users'))
     #
     # tags = orm.relationship('Tag', secondary = article2tag, backref='Article')
     #
     # comments = orm.relationship('Comment', foreign_keys='Comment.id_article')

     def __repr__(self):
        return "<Article(slug='{}',title='{}',id_category='{}',id_user='{}',)>".format(
            self.slug, self.title, self.id_category, self.id_user)


class Tag(Base):
     __tablename__ = 'tags'

     id = Column(String(10), primary_key=True)
     id_article = Column(String, unique=False)
     tag = Column(String, unique=False)


     def __init__(self, id, id_article, tag):
         self.id = id
         self.id_article = id_article
         self.tag = tag

     def __repr__(self):
        return "<Article(id='{}',id_article='{}',tag='{}')>".format(
            self.id, self.id_article, self.tag)

class ip_2_comment(Base):
    __tablename__ = 'ip_2_commnet'

    ip = Column(String, primary_key=True)
    # id_author = Column(String, ForeignKey('users.id'), index=True)
    id_comment = Column(String, index=True)
    email_of_non_registerd_user = Column(String, unique=False)
    name_of_non_registered_user = Column(String, unique=False)

    # article = relationship('Article',   backref=orm.backref('articles'))

    def __init__(self, ip, id_comment, email_of_non_registerd_user, name_of_non_registered_user):
        self.ip = ip
        self.id_comment = id_comment
        self.email_of_non_registerd_user = email_of_non_registerd_user
        self.name_of_non_registered_user = name_of_non_registered_user



class Comment(Base):
    __tablename__ = 'comments'

    id = Column(String(10), primary_key=True)
    id_article = Column(String)
    id_user = Column(String, nullable=True)
    # id_article = Column(String, ForeignKey('articles.id'), index=True)
    from datetime import datetime
    comment = Column(Text, unique=False)
    created = Column(DateTime, unique=False)
    # article = relationship('Article',   backref=orm.backref('articles'))

    def __init__(self, id, id_article, id_user,id_guest, comment):
        self.id = id
        self.id_article = id_article
        self.id_user = id_user
        self.id_guest = id_guest
        self.created = datetime.datetime.now()
        self.comment = comment

    def __repr__(self):
        return "<Article(id='{}',id_article='{}',id_user='{}', email_of_non_registerd_user='{}', name_of_non_registered_user='{}', comment='{}', created='{}')>".format(
            self.id, self.id_article, self.id_user, self.email_of_non_registerd_user,  self.comment, self.created)


class Category(Base):
    __tablename__ = 'category'

    id = Column(String(10), primary_key=True)


    def __init__(self, id, id_article, id_user, email_of_non_registerd_user, name_of_non_registered_user, comment, created):
        self.id = id


    def __repr__(self):
        return "{}".format(self.id)


class s_articles(Base):
    __tablename__ = 's_articles'

    id = Column(String(16), primary_key=True)
    active_stage = Column(String(3), index=True, nullable=False)

    # __table_args__ = (Index('_s_users_idx0', 'active_stage'),)

    def __init__(self, _id, active_stage):
        self.id = _id
        self.active_stage = active_stage


class s_tags(Base):
    __tablename__ = 's_tags'

    id = Column(String(16), primary_key=True)
    active_stage = Column(String(3), index=True, nullable=False)

    # __table_args__ = (Index('_s_users_idx0', 'active_stage'),)

    def __init__(self, _id, active_stage):
        self.id = _id
        self.active_stage = active_stage


class s_comments(Base):
    __tablename__ = 's_comments'

    id = Column(String(16), primary_key=True)
    active_stage = Column(String(3), index=True, nullable=False)

    # __table_args__ = (Index('_s_users_idx0', 'active_stage'),)

    def __init__(self, _id, active_stage):
        self.id = _id
        self.active_stage = active_stage


class Sequencer(Base):
    __tablename__ = 'sequencer'

    id = Column(String(2), primary_key=True)
    s_partition = Column(String(2), nullable=False)
    size = Column(SmallInteger, nullable=False)
    active_stage = Column(String(3), nullable=False)
    check_sum_size = Column(SmallInteger, nullable=False)
    name = Column(String(64), nullable=False, unique=True)
    type = Column(String(16), nullable=False)
    s_table = Column(String(64), nullable=False, unique=True)
    ordered = Column(Boolean, nullable=False, default=False)

    def __init__(self, _id, s_partition, active_stage, size, check_sum_size, name, _type, s_table, ordered=False):
        self.id = _id
        self.s_partition = s_partition
        self.active_stage = active_stage
        self.size = size
        self.check_sum_size = check_sum_size
        self.name = name
        self.type = _type
        self.s_table = s_table
        self.ordered = ordered


class s_users(Base):
    __tablename__ = 's_users'

    id = Column(String(10), primary_key=True)
    active_stage = Column(String(3), index=True, nullable=False)

    # __table_args__ = (Index('_s_users_idx0', 'active_stage'),)

    def __init__(self, _id, active_stage):
        self.id = _id
        self.active_stage = active_stage


class s_session_token(Base):
    __tablename__ = 's_session_token'

    id = Column(String(64), primary_key=True)
    active_stage = Column(String(3), index=True, nullable=False)

    # __table_args__ = (Index('_s_session_token_idx0', 'active_stage'),)

    def __init__(self, _id, active_stage):
        self.id = _id
        self.active_stage = active_stage


class s_hash_2_params(Base):
    __tablename__ = 's_hash_2_params'

    id = Column(String(64), primary_key=True)
    active_stage = Column(String(3), index=True, nullable=False)

    # __table_args__ = (Index('_s_hash_2_params_idx0', 'active_stage'),)

    def __init__(self, _id, active_stage):
        self.id = _id
        self.active_stage = active_stage


Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

for _s in [
    ('u', '00', '000', 4, 0, 'users', 'STR', 's_users', False),
    ('a', '00', '000', 10, 0, 'articles', 'STR', 's_articles', False),
    ('t', '00', '000', 10, 0, 'tag', 'STR', 's_tags', False),
    ('c', '00', '000', 10, 0, 'comments', 'STR', 's_comments', False),
    ('s', '00', '000', 58, 0, 'session_token', 'STR', 's_session_token', False),
    ('h', '00', '000', 58, 0, 'hash_2_params', 'STR', 's_hash_2_params', False)]:
    _seq = Sequencer(*_s)

    session.add(_seq)
session.commit()