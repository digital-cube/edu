import random

from db import *
from sequencer import seq
import sqlalchemy
import re

class UsernameAlreadyExistsException(BaseException):
    pass

class UserPasswordNotStrongEnough(BaseException):
    pass

class InvalidSlugException(BaseException):
    pass

class UserPasswordNotValid(BaseException):
    pass


class Blog(object):

    def __init__(self, session):
        self.session = session

    #TODO: napravite da mora da prihvata bar jedno malo, bar jedno veliko slovo, bar jedan interpunkciski karakter
    #TODO: bar jedan broj i minimum 8 karaktera.
    #TODO: pokrite ovu funkciju testovima samo za nju, kao i create_user sa setom istih testova


    def check_password(self, password):
        number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        character = ['.', '?', '!', ',', ';',':','-','_','”','„','(',')','[',']','{','}','%', '#','@','$','%','^','&']
        three = ['123','asd','qwe','zxc']


        if len(password) < 8:
            return False

        if (password[0:len(password)]).isdigit():
            return False

        if password[0:3] in three:
            return False

        for i in password:
            if i in range(ord('A'),ord('Z')) or i in range(ord('a'),ord('z')) or i in character or i in number:
                return True
        return False


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
        if not self.check_slug(slug):
            return False

        return not self.is_slug_in_db(slug)

    def make_slug(self, title):
        return ''.join([c if (c>='a' and c<='z') or c in ('.', ' ', '-', '_') else '' for c in title.lower()]).\
            replace(' ','-')

    def create_user(self, email, password, fname=None, lname=None):
        author = User(seq('users'), email, password, fname, lname)

        if not self.check_password(password):
            raise UserPasswordNotValid

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

    def add_post(self, id_author, slug, title, content):

        post = Post(seq('posts'), id_author, slug, title, content)

        if not self.check_slug_aviability(slug):
            raise InvalidSlugException

        self.session.add(post)
        try:
            self.session.commit()
        except sqlalchemy.exc.IntegrityError:

            self.session.rollback()


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