
import db
import sqlalchemy.exc
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

class SlugNotValidException(BaseException):
    pass

class TitleNotValidException(BaseException):
    pass

class TitleAndSlugNotValidException(BaseException):
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


def randomword(length):
    import random
    randomString = ""
    for i in range(10):
        randomString += (str(chr(random.randint(97, 122))))  # intended to put tab space.
    return randomString



def add_user(email):

    check_email(email)

    try:
        import seq
        aid = randomword(10)
        user = db.User(aid,email)
        db.session.add(user)
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        raise UserAlreadyExistsException

    return True

def check_slug_and_title(title,slug):
    not_allowed_char = ('<', '>', '{', '}', '%', '#',
                        '!', '*', '(', ')', '+', '=',
                        '$', '&', '^', '±', '§', '/',
                         ':', ';', ',', '|')

    for i in not_allowed_char:
        if slug.find(i) != -1:
            raise SlugNotValidException

    if slug.find(' ') != -1:
        raise SlugNotValidException

    for i in not_allowed_char:
        if title.find(i) != -1:
            raise TitleNotValidException

    return True




    #
    # for i in not_allowed_char:
    #     if title.find(i):
    #         raise ArticleTitleException


def add_article(slug, title, id_category, number_of_likes, number_of_comments):

    # check_title(title)
    if not check_slug_and_title(title,slug):
        raise TitleAndSlugNotValidException

    if len(slug)!=0:
        slug = title.replace(' ', '-')

    try:
        import seq
        id = randomword(10)
        article = db.Article(id, slug, title, id_category, number_of_likes, number_of_comments)
        db.session.add(article)
        db.session.commit()
        print(article)

    except sqlalchemy.exc.IntegrityError:
        raise ArticleAlreadyExistsException
    return True


#
# def edit_user(email):
#
#     check_email(email)
#
#     try:
#         user = db.User(email)
#         db.session = user.update().where(users.c.id == 5). \
#             values(name='user #5')
#
#         db.session.commit()
#     except sqlalchemy.exc.IntegrityError:
#         raise UserAlreadyExistsException
#
#     return True
