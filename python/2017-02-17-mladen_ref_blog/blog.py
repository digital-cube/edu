import random

from db import session, User, Post, Tag, Comment,Guest
from sequencer import seq
import sqlalchemy
import re

class UsernameAlreadyExistsException(BaseException):
    pass

class UserPasswordNotStrongEnough(BaseException):
    pass

class InvalidSlugException(BaseException):
    pass

class UserFirstLastNameNotStrongEnough(BaseException):
    pass

class UserEmailNotStrongEnough(BaseException):
    pass

class PostDoesntExist(BaseException):
    pass

class PostEditException(BaseException):
    pass

class ArticleDoesntExist(BaseException):
    pass

class CommentDoesntExist(BaseException):
    pass

class ErrorEditingCommentException(BaseException):
    pass

class EmailNotStrongEnough(BaseException):
    pass

class EmailNotValid(BaseException):
    pass


class Blog(object):

    def __init__(self, session):
        self.session = session



    def check_password(self, password):
        return re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,22}', password) != None

    def check_user_username(self,username):
        return re.match('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', username) != None

    def check_email(self,email):
        return re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

    def randomstr(self,length):
        import random
        random_string = ''
        for i in range(length):
            random_string += (str(chr(random.randint(97, 122))))
        return random_string

    def is_slug_in_db(self, slug):

        res = self.session.query(Post.id).filter(
            Post.slug == slug
        ).one_or_none()

        return res != None

    def get_post_by_slug(self, slug):
        return self.session.query(Post).filter(
            Post.slug == slug
        ).one_or_none()

    # def get_all_users(self):
    #     return self.session.query(User).all()

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

        if not self.check_user_username(email):
            raise UserEmailNotStrongEnough

        try:
            self.session.add(author)
            self.session.commit()
        except sqlalchemy.exc.IntegrityError:
            self.session.rollback()

            raise UsernameAlreadyExistsException

    def create_guest(self,email, fname=None, lname=None ):
        guest = Guest(seq('guests'), email, fname, lname)

        if not self.check_email(email):
            raise EmailNotStrongEnough

        try:
            self.session.add(guest)
            self.session.commit()
        except sqlalchemy.exc.IntegrityError:
            self.session.rollback()
            return False
        return guest.id

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
            slug = self.make_slug(title)

            if not self.check_slug_aviability(slug):
                # random str
                # slug = slug+'-'+self.randomstr(5)
                slug = slug+'-1'

        post = Post(seq('posts'), author, slug, title, content)

        self.session.add(post)
        try:
            self.session.commit()
        except sqlalchemy.exc.IntegrityError:

            self.session.rollback()

        return post

    def delete_post(self, id_post):
        res = self.get_post(id_post)
        if not res:
            raise PostDoesntExist

        res = self.session.query(Post).filter(Post.id == id_post).delete()

        try:
            self.session.commit()
        except Exception:
            self.session.rollback()
            raise PostDoesntExist

        return res

    def delete_comment(self, id_comment):
        res = self.get_comment(id_comment)
        if not res:
            raise PostDoesntExist

        res = self.session.query(Comment).filter(Comment.id == id_comment).delete()

        try:
            self.session.commit()
        except Exception:
            self.session.rollback()
            raise PostDoesntExist

        return res

    def make_tag_if_not_exists_and_return_tag_object(self, tag_name):
        res = self.get_tag(tag_name)
        if not res:
            res = Tag(seq('tags'), tag_name)
            self.session.add(res)

        return res

    def get_comment(self, id_comment):
        return self.session.query(Comment).filter(Comment.id == id_comment).one_or_none()

    def edit_comment(self, id_comment, text):
        comment = self.get_comment(id_comment)
        if not comment:
            raise CommentDoesntExist
        try:
            comment.comment_text = text
            self.session.commit()
        except:
            self.session.rollback()
            raise ErrorEditingCommentException

        return True


    def edit_post(self, id, title, content):
        res = self.get_post(id)
        if not res:
            raise PostDoesntExist

        res.title = title
        res.content = content

        try:
            session.commit()
        except sqlalchemy.exc.IntegrityError:
            res.session.rollback()
            raise PostEditException

        return res

    def get_tag(self, tag_name):
        tag_name = Tag.fix_tag_name(tag_name)
        return self.session.query(Tag).filter(
            Tag.name == tag_name
        ).one_or_none()

    def get_user_post(self):
        return

    def get_all_post(self,date=None,word=None):
        if date:
            return self.session.query(Post).filter(Post.posted.like("%"+date+"%")).all()

        if word:
            return self.session.query(Post).filter(Post.title.like("%"+word+"%")).all()

        return self.session.query(Post).all()

    def get_post(self, id):
        return self.session.query(Post).filter(
            Post.id == id
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