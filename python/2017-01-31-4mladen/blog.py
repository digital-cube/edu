import db
import sqlalchemy.exc
from sqlalchemy import select


class UserDoesntExist(BaseException):
    pass


class UsersDoesntExist(BaseException):
    pass


class UserAlreadyExistsException(BaseException):
    pass


class EmailNotValidException(BaseException):
    pass


class SlugNotValidException(BaseException):
    pass


class EmailNotValidSize(BaseException):
    pass


class ArticleEmptyFields(BaseException):
    pass


class ArticleAlreadyExistsException(BaseException):
    pass


class ArticleTitleException(BaseException):
    pass


class StringNotValidException(BaseException):
    pass


class TitleNotValidException(BaseException):
    pass


class TitleNotValidException(BaseException):
    pass


class ArticleDoesntExist(BaseException):
    pass

class TagsDoesntExist(BaseException):
    pass


class TagsInsertErrorException(BaseException):
    pass


class TagsNotValidException(BaseException):
    pass


class CommentAlreadyExistsException(BaseException):
    pass


def check_email(email):

    not_allowed_char = ('<', '>', '{', '}', '%', '#',
                        '!', '*', '(', ')', '+', '=',
                        '$', '&', '^', '±', '§', '/',
                        '"', "'", ':', ';', ',', '|')
    allowed_char = ('@', '.', '-', '_', '1', '2','3','4','5','6','7','8','9','0')

    # check email size from 5 - 30 characters
    if len(email) > 30 or len(email) < 5:
        raise EmailNotValidSize

    # check is doesn't exist @ in email
    if email.find('@') == -1:
        raise EmailNotValidException

    # check is @ in email two or more times
    if email.count('@') >= 2:
        raise EmailNotValidException

    # check some from not allowed char on end of email  - from tuple allowed_char
    for i in allowed_char:
        if email[-1] == i:
            raise EmailNotValidException

    # check is not allowed char in email  - from tuple not_allowed_char
    for i in not_allowed_char:
        if email.find(i) != -1:
            raise EmailNotValidException


def check_slug_and_title(string):
    not_allowed_char = ('<', '>', '{', '}', '%', '#',
                        '!', '*', '(', ')', '+', '=',
                        '$', '&', '^', '±', '§', '/',
                         ':', ';', ',', '|')
    if string == ' ':
        return False

    for i in not_allowed_char:
        if string.find(i) != -1:
            return False

    return True


def check_tags(tags):
    if not isinstance(tags, set):
        raise TagsNotValidException
    return True


def randomword(length, type):
    import random
    random_string = ""

    if type == 'id':
        for i in range(length):
            random_string += (str(chr(random.randint(97, 122))))  # intended to put tab space.

    if type == 'words':
        a = ['hello', 'world', 'welcome', 'people']
        for i in range(length):
            random_string += random.choice(a)

    return random_string


#done
def add_user(email):

    check_email(email)

    try:
        import seq
        aid = randomword(10,'id')
        user = db.User(aid, email)
        db.session.add(user)
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        raise UserAlreadyExistsException

    return aid


#done
def generate_slug(slug):
    res = db.session.query(db.Article).filter(db.Article.slug.like("%"+slug+"%"))
    if not res or res.count() == 0:
        return slug
    num = res.count()
    # print(type(num),num)
    return slug + '-' + str(num)


#done
def add_article(slug, title, id_user, id_category, content):

    if not check_slug_and_title(title):
        raise TitleNotValidException

    if not check_slug_and_title(slug):
        raise SlugNotValidException

    if len(slug) == 0:
        slug = title.replace(' ', '-')
        slug = generate_slug(slug)

    slug.lower()


    try:
        aid = randomword(10,'id')

        article = db.Article(aid,id_user, slug, title, id_category, content)
        db.session.add(article)
        db.session.commit()

    except sqlalchemy.exc.IntegrityError:
        db.session.rollback()
        raise ArticleAlreadyExistsException

    return aid


#done- to do tests
def get_user(id):
    try:
        res = db.session.query(db.User).filter(db.User.id == id)
    except sqlalchemy.exc.IntegrityError:
        db.session.rollback()
        raise UserDoesntExist

    if not res or res.count() == 0:
        raise UserDoesntExist

    return res


#done- to do tests
def get_users():
    try:
        res = db.session.query(db.User)
    except sqlalchemy.exc.IntegrityError:
        db.session.rollback()
        raise UsersDoesntExist

    if not res or res.count() == 0:
        raise UsersDoesntExist

    return res


#done- to do tests
def get_tags(id_article):
    try:
        res = db.session.query(db.Tags).filter(db.Tags.id_article == id_article)
    except sqlalchemy.exc.IntegrityError:
        db.session.rollback()
        raise TagsDoesntExist

    if not res or res.count() == 0:
        raise TagsDoesntExist

    return res


#done- to do tests
def get_article(id_article):
    try:
        res = db.session.query(db.Article).filter(db.Tags.id_article == id_article)
    except sqlalchemy.exc.IntegrityError:
        db.session.rollback()
        raise ArticleDoesntExist

    if not res or res.count() == 0:
        raise ArticleDoesntExist

    return res

#done - to do tests
def get_articles():
    try:
        res = db.session.query(db.Article)
    except sqlalchemy.exc.IntegrityError:
        db.session.rollback()
        raise ArticleDoesntExist

    if not res or res.count() == 0:
        raise ArticleDoesntExist

    return res


#done
def delete_article(id):
    try:
        res = db.session.query(db.Article).filter(db.Article.id == id)
    except sqlalchemy.exc.IntegrityError:
        db.session.rollback()
        raise ArticleDoesntExist

    if not res or res.count() == 0:
        raise ArticleDoesntExist

    try:
        db.session.query(db.Article).filter(db.Article.id == id).delete()
        db.session.commit()

    except sqlalchemy.exc.IntegrityError:
        db.session.rollback()
        raise ArticleDoesntExist

    return True


#done
def add_edit_tags(id_article, tags):

    try:
        article_res = db.session.query(db.Article.id).filter(db.Article.id == id_article).one_or_none()
        if not article_res or len(article_res) == 0:
            raise ArticleDoesntExist

    except sqlalchemy.exc.IntegrityError:
        db.session.rollback()
        raise ArticleAlreadyExistsException

    try:
        tag_res = db.session.query(db.Tags).filter(db.Tags.id_article == id_article).all()
    except sqlalchemy.exc.IntegrityError:
        db.session.rollback()
        raise TagsDoesentExist

    if not check_tags(tags):
        raise TagsNotValidException

    if tag_res or len(tag_res) != 0:
        for i in tag_res:

            if i.tag in tags:
                tags.remove(i.tag)
    try:
        for tag in tags:
            aid = randomword(10, 'id')
            tag = db.Tags(aid, id_article, tag)
            db.session.add(tag)
            db.session.commit()

    except sqlalchemy.exc.IntegrityError:
        db.session.rollback()
        raise TagsInsertErrorException

    return True


#not done - to do tests
def edit_num_of_likes(id_article, num):
    try:
        article_res = db.session.query(db.Article).filter(db.Article.id == id_article).one_or_none()
        if not article_res or len(article_res) == 0:
            raise ArticleDoesntExist

    except sqlalchemy.exc.IntegrityError:
        db.session.rollback()
        raise ArticleAlreadyExistsException

    #Update broj lika
    # article = article.where(db.Article.id == id)


#not done
def add_comment(id_user,id_article, content):
    #we need to test is correct content of commentar
    return True
    try:
        aid = randomword(10,'id')

        comment = db.Comment(aid,id_user,id_article, content)
        db.session.add(comment)
        db.session.commit()

    except sqlalchemy.exc.IntegrityError:
        db.session.rollback()
        raise CommentAlreadyExistsException

    # return aid


#not done
def edit_article(id, title, id_category, content):
   pass
