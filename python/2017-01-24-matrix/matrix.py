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

class NotPossibleToMakeLeftLowerTriangle(Exception):
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
                x = self.data[r][c]
                if abs(x)<0.00001:
                    x = 0
                res += '{:5} '.format(round(x,2))
            res += '\n'

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

    def make_zeros_below_diagonal(self):
        m = min(self.width, self.height)
        for d in range(0, m):
            self.make_zeros_below_diagonal_at_d(d)


    def make_zeors_before_diagonal_at_d(self, d):

        if self.data[d][d] == 0:
            swapped = False
            for row in range(d-1, 0, -1):
                if self.data[row][d] != 0:
                    self.swap_rows(d, row)
                    swapped = True
                    break

            if not swapped:
                raise NotPossibleToMakeLeftLowerTriangle


        for row in range(d-1, -1, -1):
            x = -1 * self.data[row][d] / self.data[d][d]
            self.multiply_row_and_add_to_row(d, x, row)

    def make_zeros_below_diagonal_at_d(self, d):

        if self.data[d][d] == 0:
            swapped = False
            for row in range(d+1,self.height):
                if self.data[row][d] != 0:
                    self.swap_rows(d, row)
                    swapped = True
                    break

            if not swapped:
                raise NotPossibleToMakeLeftLowerTriangle


        for row in range(d+1,self.height):
            x = -1 * self.data[row][d] / self.data[d][d]
            self.multiply_row_and_add_to_row(d, x, row)

    # TODO: Make unit tests for this
    def make_upper_zero_triangle_for_first_square_sub_matrix(self):
        m = min(self.width, self.height)
        for d in range(m - 1, 0, -1):
            self.make_zeors_before_diagonal_at_d(d)

class SquareMatrix(Matrix):

    def __init__(self, dimension, data=None):
        super(SquareMatrix, self).__init__(dimension, dimension, data)


    ## const methods

    def get_dimension(self):
        return self.get_height()

    def make_upper_zero_triangle(self):
        for d in range(self.width - 1, 0, -1):
            self.make_zeors_before_diagonal_at_d(d)

    def invert(self):

        M = Matrix(self.height, self.width * 2)

        for row in range(self.height):
            for col in range(self.width):
                M.data[row][col] = self.data[row][col]
            M.data[row][row+self.width] = 1

        M.make_zeros_below_diagonal()

        M.make_upper_zero_triangle_for_first_square_sub_matrix()

        for row in range(M.height):
            x = M.data[row][row]
            if x!=1:
                for c in range(row, M.width):
                    M.data[row][c] /= x

        I = SquareMatrix(self.height)

        for row in range(self.height):
            for col in range(self.width-1, M.width):
                I.data[row][col-self.width] = M.data[row][col]

        self.data = I.data
