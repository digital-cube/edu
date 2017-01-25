class InvalidDataDimensions(Exception):
    pass

class InvalidMatrixDimensions(Exception):
    pass


class InvalidDataType(Exception):
    pass


class Matrix(object):

    def __init__(self, height, width, data=None):

        self.height = height
        self.width = width

        if not data:
            self.data = [[0 for _ in range(self.width)] for _ in range (self.height)]
        else:

            if len(data) != self.height:
                raise InvalidDataDimensions

            for row in data:
                if len(row) != self.width:
                    raise InvalidDataDimensions

                for x in row:
                    if type(x) not in (type(1), type(1.0)):
                        raise InvalidDataType

            self.data = data

    ## Const methods

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_data(self):
        return self.data

    ## Static methods

    @staticmethod
    def multiplicate(A, B):

        if A.get_width() != B.get_height():
            raise InvalidMatrixDimensions

        C = Matrix(A.get_height(), B.get_width())

        for row in range(A.get_height()):
            for col in range(B.get_width()):
                s = 0
                for i in range(A.get_width()):
                    s += A.data[row][i]*B.data[i][col]

                C.data[row][col] = s

        return C

    ## Mutable methods

    def scalar_multiplication(self, x):

        self.data = [[i*x for i in row] for row in self.data]

    def add_matrix(self, M):

        if self.height != M.height or self.width != M.width:
            raise InvalidMatrixDimensions

        for row in range(self.height):
            for column in range(self.width):
                self.data[row][column] += M.data[row][column]

    def transpose(self):

        T = Matrix(self.get_width(), self.get_height())

        for row in range(self.height):
            for col in range(self.width):
                T.data[col][row] = self.data[row][col]

        self.width = T.width
        self.height = T.height
        self.data = T.data


class SquareMatrix(Matrix):

    def __init__(self, dimension, data=None):
        super(SquareMatrix, self).__init__(dimension, dimension, data)


    ## const methods

    def get_dimension(self):
        return self.get_height()