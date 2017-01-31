
import db
import sqlalchemy.exc

class UserAlreadyExistsException(BaseException):
    pass

class EmailNotValidException(BaseException):
    pass

def add_user(email):

    if email.find('@')==-1:
        raise EmailNotValidException

    try:
        user = db.User(email)
        db.session.add(user)
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        raise UserAlreadyExistsException

    return True
