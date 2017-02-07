import random

from db import session, User
from sequencer import seq

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