class InvalidDataDimensions(Exception):
    pass

class InvalidMatrixDimensions(Exception):
    pass

class InvalidRow(Exception):
    pass

class InvalidColumn(Exception):
    pass

class InvalidDataType(Exception):
    pass

class InvalidInputDataType(Exception):
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

    def __str__(self):
        res = ''
        for r in range(self.height):
            for c in range(self.width):
                res+='{:5} '.format(self.data[r][c])
            res+='\n'

        return res

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

    def multiply_row_and_add_to_row(self, source_row, x, destination_row):

        if source_row == destination_row:
            raise InvalidInputDataType

        if source_row < 0 or source_row >= self.height:
            raise InvalidRow

        if destination_row < 0 or destination_row >= self.height:
            raise InvalidRow

        if type(x) not in (type(1), type(1.0)):
            raise InvalidInputDataType

        for c in range(self.width):
            self.data[destination_row][c] += self.data[source_row][c] * x

    def swap_rows(self, row1, row2):

        if row1 == row2:
            raise InvalidInputDataType

        if row1 < 0 or row1 >= self.height:
            raise InvalidRow

        if row2 < 0 or row2 >= self.height:
            raise InvalidRow

        self.data[row1], self.data[row2] = self.data[row2], self.data[row1]

    def gaus1(self, d):

        for row in range(d+1,self.height):
            x = -1 * self.data[row][d] / self.data[d][d]
            self.multiply_row_and_add_to_row(d, x, row)

class SquareMatrix(Matrix):

    def __init__(self, dimension, data=None):
        super(SquareMatrix, self).__init__(dimension, dimension, data)


    ## const methods

    def get_dimension(self):
        return self.get_height()