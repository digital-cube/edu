# coding= utf-8

from base.application.components import Base
from base.application.components import api
from base.application.components import params
from base.application.components import authenticated
import json
import src.lookup.user_roles as role
from datetime import date
import base.common.orm


def change_user_data(id, first_name, last_name, birthday, src_obj):

    user, _session = base.common.orm.get_orm_model('users')

    u = _session.query(user).filter(user.id == id).one_or_none()

    if not u:
        return src_obj.error("User not exists")

    changed = []
    if first_name and u.first_name != first_name:
        u.first_name = first_name
        changed.append('first_name')
    if last_name and u.last_name != last_name:
        u.last_name = last_name
        changed.append('last_name')
    if birthday:
        # data = json.loads(u.data) if u.data else {}
        # user_bday = data['birthday'] if 'birthday' in data else None

        data = {}
        if u.data:
            data = json.loads(u.data)

        user_bday = None

        if 'birthday' in data:
            user_bday = data['birthday']

        ######################## zamena za gornji ternarni operator

        if str(birthday) != user_bday:
            data['birthday'] = str(birthday)
            u.data = json.dumps(data)
            changed.append('birthday')

    if changed:
        _session.commit()

    return src_obj.ok({'changed': changed})


@api(URI='/users')
@authenticated()
class Users(Base):

    @params(
        {'name': 'order', 'type': str, 'required': False, 'doc': 'first/last/birthday or days_till_birthday', },
    )
    def get(self, order):
        user, _session = base.common.orm.get_orm_model('users')

        db_order = None

        if order == 'first':
            db_order = user.first_name
        if order == 'last':
            db_order = user.last_name

        all_users = []
        for u in _session.query(user).order_by(db_order).all():
            birthday = None
            if u.data:
                data = json.loads(u.data) if u.data else {}
                birthday = data['birthday'] if 'birthday' in data else None

            all_users.append(
                {'id': u.id,
                 'email': u.auth_user.username,
                 'first_name': u.first_name,
                 'last_name': u.last_name,
                 'birthday': birthday,
                 }
            )

        def fff(k):
            return k['birthday']

        if order == 'birthday':
            all_users.sort(key=fff)

        if order == 'days_till_birthday':
            return self.error('Not Implemented')


        return self.ok({'users':all_users})

    @params(
        {'name': 'first_name', 'type': str, 'required': False, 'doc': 'First name', },
        {'name': 'last_name', 'type': str, 'required': False, 'doc': 'Last name', },
        {'name': 'birthday', 'type': date, 'required': False, 'doc': 'Birthday', },
    )
    def patch(self, first_name, last_name, birthday):

        return change_user_data(self.auth_user.id, first_name, last_name, birthday, self)


@api(URI='/users/:id')
class SingleUser(Base):

    @authenticated()
    def get(self, id):
        user, _session = base.common.orm.get_orm_model('users')

        u = _session.query(user).filter(user.id == id).one_or_none()

        if not u:
            return self.error("User not exists")

        return self.ok({'email': u.auth_user.username,
                        'first_name': u.first_name,
                        'last_name': u.last_name,})

    @authenticated(role.ADMIN)
    @params(
        {'name': 'id','type': str, 'required': True, 'doc': 'id',},
        {'name': 'first_name','type': str,'required': False, 'doc': 'First name',},
        {'name': 'last_name','type': str,'required': False,'doc': 'Last name',},
        {'name': 'birthday','type': date,'required': False, 'doc': 'Birthday',},
    )
    def patch(self, id, first_name, last_name, birthday):

        return change_user_data(id, first_name, last_name, birthday, self)
