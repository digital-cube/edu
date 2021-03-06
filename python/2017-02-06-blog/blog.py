import random

from db import session, User, Post, Tag
from sequencer import seq
import sqlalchemy
import re

class UsernameAlreadyExistsException(BaseException):
    pass

class UserPasswordNotStrongEnough(BaseException):
    pass

class InvalidSlugException(BaseException):
    pass


class Blog(object):

    def __init__(self, session):
        self.session = session

    #TODO: napravite da mora da prihvata bar jedno malo, bar jedno veliko slovo, bar jedan interpunkciski karakter
    #TODO: bar jedan broj i minimum 8 karaktera.
    #TODO: pokrite ovu funkciju testovima samo za nju, kao i create_user sa setom istih testova

    def check_password(self, password):
        return len(password) > 2

    def is_slug_in_db(self, slug):

        res = self.session.query(Post.id).filter(
            Post.slug == slug
        ).one_or_none()

        return res != None

    def get_post_by_slug(self, slug):
        return self.session.query(Post).filter(
            Post.slug == slug
        ).one_or_none()

    def get_user_by_id(self, id):
        return self.session.query(User).filter(
            User.id == id
        ).one_or_none()

    def check_slug(self, slug):
        return re.match('^[\.a-z0-9\-_]+$', slug) != None

    def check_slug_aviability(self, slug):
        return not self.is_slug_in_db(slug)

    def make_slug(self, title):
        return ''.join([c if (c>='a' and c<='z') or c in ('.', ' ', '-', '_') else '' for c in title.lower()]).\
            replace(' ','-')

    def create_user(self, email, password, fname=None, lname=None):
        author = User(seq('users'), email, password, fname, lname)

        if not self.check_password(password):
            raise UserPasswordNotStrongEnough

        try:
            self.session.add(author)
            self.session.commit()
        except sqlalchemy.exc.IntegrityError:
            self.session.rollback()

            raise UsernameAlreadyExistsException

    def login_user(self, email, password):

        res = self.session.query(User.id).filter(
            User.username == email,
            User.password == password
        ).one_or_none()

        if not res:
            return False

        return res[0]

    def add_post(self, author, slug, title, content):

        if not self.check_slug(slug):
            raise InvalidSlugException

        if not self.check_slug_aviability(slug):
            raise InvalidSlugException

        post = Post(seq('posts'), author, slug, title, content)

        self.session.add(post)
        try:
            self.session.commit()
        except sqlalchemy.exc.IntegrityError:

            self.session.rollback()

        return post

    def make_tag_if_not_exists_and_return_tag_object(self, tag_name):
        res = self.get_tag(tag_name)
        if not res:
            res = Tag(seq('tags'), tag_name)
            self.session.add(res)

        return res

    def get_tag(self, tag_name):
        tag_name = Tag.fix_tag_name(tag_name)
        return self.session.query(Tag).filter(
            Tag.name == tag_name
        ).one_or_none()

    def tag_it(self, post, list_of_tag_names):

        try:
            for tag_name in list_of_tag_names:
                post.add_tag(
                    self.make_tag_if_not_exists_and_return_tag_object(tag_name))

            self.session.commit()

        except Exception as e:
            self.session.rollback()

    def all_posts_tagged_with(self, tag_name):

        tag = self.get_tag(tag_name)
        if not tag:
            return []

        return tag.posts


def get_blog():

    if not hasattr(get_blog, 'blog'):
        get_blog.blog = Blog(session)

    return get_blog.blog


if __name__=="__main__":

    mladen = User(seq('users'), 'mladen@digitalcube.rs')
    aca = User(seq('users'), 'aca@digitalcube.rs')
    munira = User(seq('users'), 'munira@digitalcube.rs')

    session.add(mladen)
    session.add(aca)
    session.add(munira)
    session.commit()

    # mladen = session.query(User).filter(User.id=='uMAzOn').one_or_none()
    #
    # session.commit()