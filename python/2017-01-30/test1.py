




class A(object):

    klasna_promenljiva = 0

    def __init__(self):

        A.klasna_promenljiva += 1

    @staticmethod
    def ppp():

        print(A.klasna_promenljiva)



aaa = A()

aaa.ppp()

bbb = A()

bbb.ppp()