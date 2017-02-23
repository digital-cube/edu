import random

class SequencerUnknownTableException(BaseException):
    pass

class SequencerTooManyAttemptsToGenerateID(BaseException):
    pass

def mock_seq(id, length):

    # from mock_seq_data import l as mock_data
    from mock_seq_data import gen_seq_from_number

    if not hasattr(mock_seq, 'mocks_by_length'):
        mock_seq.mocks_by_length = {}

    if length not in mock_seq.mocks_by_length:
        mock_seq.mocks_by_length[length] = 0

    res = gen_seq_from_number(length,mock_seq.mocks_by_length[length])
    # res = mock_data[length][mock_seq.mocks_by_length[length]]
    mock_seq.mocks_by_length[length] += 1

    return id+res


def real_seq(table_id, length, cls):

    from db import session

    a = [chr(x) for x in list(range(ord('a'), ord('z')+1))+list(range(ord('A'), ord('Z')+1))]

    attempt = 0
    while True:
        random.shuffle(a)
        id = table_id + ''.join(a[:length])
        exists = session.query(cls.id).filter(cls.id == id).one_or_none()
        if not exists:
            return id

        attempt += 1
        if attempt > 50:
            raise SequencerTooManyAttemptsToGenerateID


def seq(table):

    if not hasattr(seq, 'f'):
        seq.f = None

    from db import User, Post, Tag, Comment, Guest

    m = {'users': {'length': 5, 'id': 'u', 'cls': User},
         'guests': {'length': 9, 'id': 'g', 'cls': Guest},
         'posts': {'length': 7, 'id': 'p', 'cls': Post},
         'tags':  {'length': 8, 'id': 't', 'cls': Tag},
         'comments': {'length': 6, 'id': 'c', 'cls': Comment}}

    if table not in m:
        raise SequencerUnknownTableException

    if not seq.f:
        return real_seq(m[table]['id'], m[table]['length'], m[table]['cls'])

    return seq.f(m[table]['id'], m[table]['length'])