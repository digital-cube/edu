class StackIsEmptyException(BaseException):
    pass

class QueueIsEmptyException(BaseException):
    pass

class Collection(object):
    def __init__(self):
        self.l = []

    def is_empty(self):
        return len(self.l) == 0

    def __len__(self):
        return len(self.l)


class Stack(Collection):

    def __init__(self):
        super(Stack, self).__init__()

    def push(self, x):
        self.l.append(x)

    def pop(self):
        if self.is_empty():
            raise StackIsEmptyException
        return self.l.pop()



class Queue(Collection):

    def __init__(self):
        super(Queue, self).__init__()

    def enqueue(self, x):
        self.l.insert(0, x)

    def dequeue(self):
        if self.is_empty():
            raise QueueIsEmptyException
        return self.l.pop()


def are_brackets_correct(s):

    st = Stack()

    lang = [('[', ']'), ('{', '}'), ('(', ')')]

    for c in s:
        if c in ('[','(','{'):
            st.push(c)
        else:
            try:
               x = st.pop()
            except StackIsEmptyException:
                return False

            for l in lang:
                if x == l[0] and c != l[1]:
                    return False

    return st.is_empty()
