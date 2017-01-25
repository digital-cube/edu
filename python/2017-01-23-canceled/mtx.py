import copy

class IzuzetakInvalidColRowInput(Exception):
    pass

class IzuzetakMatriceMorajuBitiIsteDimenzije(Exception):
    pass

class IzuzetakKodMnozenjaSirinaPrveMoraBitiIstaKaoVisinaDruge(Exception):
    pass

class IzuzetakUlazniParametarDataNemaDobreDimenzije(Exception):
    pass

class IzuzetakTipPodatakaNijeDobar(Exception):
    pass

class Matrica(object):

    data = None
    width = None
    height = None

    def __init__(self, width, height, data=None):

        self.width = width
        self.height = height

        if not data:
            row = [0 for _ in range(self.width)]
            self.data = [row[:] for _ in range(self.height)]
        else:

            if len(data) != self.height:
                raise IzuzetakUlazniParametarDataNemaDobreDimenzije

            for r in range(self.height):
                if len(data[r]) != self.width:
                    raise IzuzetakUlazniParametarDataNemaDobreDimenzije
                for i in range(self.width):
                    if type(data[r][i]) not in ( type(1), type(1.0) ):
                        raise IzuzetakTipPodatakaNijeDobar



            self.data = data

    def set_val(self, row, col, val):
        if row>=self.height or col>=self.width:
            raise IzuzetakInvalidColRowInput

        self.data[row][col] = val

    def get_val(self, row, col):
        if row>=self.height or col>=self.width:
            raise IzuzetakInvalidColRowInput

        return self.data[row][col]

    def skalarno_mnozenje(self, x):
        for row in range(0, self.height):
            for col in range(0, self.width):
                self.data[row][col] *= x

    @staticmethod
    def mnozenje_matrica(A, B):

        if A.width != B.height:
            raise IzuzetakKodMnozenjaSirinaPrveMoraBitiIstaKaoVisinaDruge

        C = Matrica(B.width, A.height)

        for x in range(B.width):
            for y in range(A.height):
                s = 0
                for c in range(A.width):
                    s+=A.get_val(y, c)*B.get_val(c, x)

                C.set_val(y, x, s)

        return C

    def saberi_sa(self, matB):
        if self.width != matB.width or self.height != matB.height:
            raise IzuzetakMatriceMorajuBitiIsteDimenzije

        for row in range(0,self.height):
            for col in range(0, self.width):
                self.data[row][col]+=matB.data[row][col]

    def __add__(self, M):

        kopija = copy.deepcopy(self)
        kopija.saberi_sa(M)
        return kopija

    def __mul__(self, x):

        kopija = copy.deepcopy(self)
        kopija.skalarno_mnozenje(x)
        return kopija

    def __rmul__(self, x):
        return self.__mul__(x)

    def __str__(self):
        result = ''
        for row in range(0, self.height):
            for col in range(0, self.width):
                result += '{:5} '.format(str(self.data[row][col]))
            result+='\n'

        return result



if __name__=="__main__":
    pass