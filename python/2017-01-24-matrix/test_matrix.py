
import unittest

import matrix


class TestMatrix(unittest.TestCase):

    def test_constructor_width_and_height(self):
        M = matrix.Matrix(3, 2)
        self.assertEqual(M.get_height(), 3)
        self.assertEqual(M.get_width(), 2)
        self.assertEqual(M.get_data(), [[0, 0], [0, 0], [0, 0]])

    def test_constructor_with_data(self):
        M = matrix.Matrix(3, 2, [[1, 2], [3, 4], [5, 6]])
        self.assertEqual(M.get_height(), 3)
        self.assertEqual(M.get_width(), 2)
        self.assertEqual(M.get_data(), [[1, 2], [3, 4], [5, 6]])

    def test_constructor_with_data_fail1(self):

        with self.assertRaises(matrix.InvalidDataDimensions):
            M = matrix.Matrix(1, 1, [[1, 2], [3, 4]])

        with self.assertRaises(matrix.InvalidDataDimensions):
            M = matrix.Matrix(3, 1, [[1, 2], [3, 4], [5, 6]])

        with self.assertRaises(matrix.InvalidDataType):
            M = matrix.Matrix(3, 2, [['1', 2], [3, 4], [5, 6]])

        M = matrix.Matrix(3, 2, [[1.5, 2], [3, 4], [5, 6]])
        self.assertEqual(M.get_data(), [[1.5, 2], [3, 4], [5, 6]])

    def test_scalar_multiplication(self):
        M = matrix.Matrix(3, 2, [[1.5, 2], [3, 4], [5, 6]])
        self.assertEqual(M.get_data(), [[1.5, 2], [3, 4], [5, 6]])

        M.scalar_multiplication(2)
        self.assertEqual(M.get_data(), [[3, 4], [6, 8], [10, 12]])

    def test_add_matrix_to_fail_on_dimensions(self):
        A = matrix.Matrix(3, 2, [[1.5, 2], [3, 4], [5, 6]])
        B = matrix.Matrix(2, 2, [[1, 2], [3, 4]])

        with self.assertRaises(matrix.InvalidMatrixDimensions):
            A.add_matrix(B)

        A = matrix.Matrix(3, 2, [[3, 4], [5, 6], [1, 2]])
        B = matrix.Matrix(3, 1, [[4], [4], [4]])

        with self.assertRaises(matrix.InvalidMatrixDimensions):
            A.add_matrix(B)

    def test_add_matrix_to(self):
        A = matrix.Matrix(3, 2, [[1.5, 2], [3, 4], [5, 6]])
        B = matrix.Matrix(3, 2, [[1, 2], [3, 4], [1, 6]])

        A.add_matrix(B)
        self.assertEqual(A.get_data(), [[2.5, 4], [6, 8], [6, 12]])

    def test_transponse(self):
        A = matrix.Matrix(3, 2, [[1.5, 2], [3, 4], [5, 6]])
        A.transpose()

        self.assertEqual(A.get_height(), 2)
        self.assertEqual(A.get_width(), 3)
        self.assertEqual(A.get_data(), [[1.5, 3, 5], [ 2, 4, 6]])

    def test_transponse_vmatrix(self):
        A = matrix.Matrix(3, 1, [[1], [2], [3]])
        A.transpose()

        self.assertEqual(A.get_height(), 1)
        self.assertEqual(A.get_width(), 3)
        self.assertEqual(A.get_data(), [[1, 2, 3]])

    def test_multiplicate_fail_dimensions(self):

        A = matrix.Matrix(2, 2)
        B = matrix.Matrix(4, 1)

        with self.assertRaises(matrix.InvalidMatrixDimensions):
            matrix.Matrix.multiplicate(A, B)

    def test_multiplicate1(self):
        A = matrix.Matrix(2, 3, [[1, 2, 3], [2, 3, 4]])
        B = matrix.Matrix(3, 5, [[2, 1, 1, 2, 1], [1, 2, 1, 6, 1], [3, 4, 2, 1, 2]])

        C = matrix.Matrix.multiplicate(A, B)
        self.assertEqual(C.get_height(), A.get_height())
        self.assertEqual(C.get_width(), B.get_width())

        self.assertEqual(C.data, [[13, 17, 9, 17, 9], [19, 24, 13, 26, 13]])

    def test_m2(self):
        '''
            generisati ove dve matrice

        '''
    def test_multiplicate2(self):


        A = matrix.Matrix(4, 5, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])
        B = matrix.Matrix(5, 7, [[1, 2, 3, 4, 5, 6, 7], [2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7, 8, 9],
                                 [4, 5, 6, 7, 8, 9, 0], [5, 6, 7, 8, 9, 0, 1]])
        C = matrix.Matrix.multiplicate(A, B)

        self.assertEqual(C.data, [[55, 70, 85, 100, 115, 80, 55],
                                  [130, 170, 210, 250, 290, 230, 180],
                                  [205, 270, 335, 400, 465, 380, 305],
                                  [280, 370, 460, 550, 640, 530, 430]])

    def test_multiply_row_and_add_to_row(self):

        A = matrix.Matrix(4, 5, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])

        with self.assertRaises(matrix.InvalidRow):
            A.multiply_row_and_add_to_row(3, 2, 25)

        with self.assertRaises(matrix.InvalidRow):
            A.multiply_row_and_add_to_row(35, 2, 2)

        with self.assertRaises(matrix.InvalidInputDataType):
            A.multiply_row_and_add_to_row(2, 'X', 3)

        with self.assertRaises(matrix.InvalidInputDataType):
            A.multiply_row_and_add_to_row(2, 2, 2)

        A.multiply_row_and_add_to_row(0, -6, 1)
        self.assertEqual( A.data, [[1, 2, 3, 4, 5], [0, -5, -10, -15, -20], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])


    def test_swap_rows(self):

        A = matrix.Matrix(4, 5, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])
        A.swap_rows(2, 3)
        self.assertEqual(A.data, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [16, 17, 18, 19, 20], [11, 12, 13, 14, 15]])

    def test_make_zeros_below_diagonal_at_d_fail1(self):
        A = matrix.Matrix(4, 5, [[0, 2, 3, 4, 5], [0, 7, 8, 9, 10], [0, 12, 13, 14, 15], [0, 17, 18, 19, 20]])

        with self.assertRaises(matrix.NotPossibleToMakeLeftLowerTriangle):
            A.make_zeros_below_diagonal_at_d(0)

    def test_make_zeors_before_diagonal_at_d(self):
        A = matrix.Matrix(4, 5, [[1, 2, 3, 4, 5],[2, 2, 2, 2, 5],[3, 3, 4, 5, 6],[2, 2, 3, 0, 5]])

        print(A)
        A.make_zeors_before_diagonal_at_d(3)

        print(A)

    def test_make_zeros_below_diagonal_at_d_1(self):
        A = matrix.Matrix(4, 5, [[1, 2, 3, 4, 5],[2, 2, 2, 2, 5],[3, 3, 4, 5, 6],[2, 2, 3, 4, 5]])
        A.make_zeros_below_diagonal_at_d(0)
        self.assertEqual(A.data, [[1, 2, 3, 4, 5], [0, -2, -4, -6, -5], [0, -3, -5, -7, -9],[0, -2, -3, -4, -5]])

    # TODO: refaktorisati tako da radi ispravan donji trooguao, jer smo
    # TODO: zakljucili da pravimo donji trapez a to nije trougao
    def test_make_zeros_below_diagonal(self):
        A = matrix.Matrix(4, 5, [[1, 2, 3, 4, 5], [2, 2, 2, 2, 5], [3, 3, 4, 2, 6], [2, 2, 3, 4, 5]])
        A.make_zeros_below_diagonal()
        print(A.make_zeros_below_diagonal)

    def test_make_zeros_below_diagonal(self):
        A = matrix.Matrix(4, 8, [[2, 3, 1, 1, 2, 3, 4, 5], [2, 2, 2, 5, 2, 1, 2, 5], [3, 3, 4, 2, 2, 1, 3, 6], [2, 2, 3, 4, 5, 1, 1.2, 1.5]])
        A.transpose()
        print(A)
        A.make_zeros_below_diagonal()
        print(A)

        # DA = []
        # DB = []
        # A = matrix.Matrix(4, 5, DA)
        # B = matrix.Matrix(5,2, DB)
        # s = 1
        #
        # for row in range(A.get_height()):
        #     DAl=[]
        #     for col in range(A.get_width()):
        #         DAl.append(s)
        #         s+=1
        #     DA.append(DAl)
        # print(DA)
        #
        # for row in range(B.get_height()):
        #     DBl = []
        #     for col in range(B.get_width()):
        #         DBl.append(s)
        #         s+=1
        #     DB.append(DBl)
        #
        # print("DB vrednost\n")
        # print(DB)
        # C = matrix.Matrix.multiplicate(A, B)
        # self.asgit sertEqual(C.get_height(), A.get_height())
        # self.assertEqual(C.get_width(), B.get_width())
        # self.assertEqual(C.data, [[395, 410], [1020, 1060],[1645, 1710],[2270, 2360]])



        # kraci primer
        DA=[]

        for row in range(4):
            DA.append([5*row+i+1 for i in range(5)])
        print(DA)



class TestSquareMatrix(unittest.TestCase):

    def test_constructor_width_and_height(self):
        M = matrix.SquareMatrix(3)
        self.assertEqual(M.get_dimension(), 3)
        self.assertEqual(M.get_width(), 3)
        self.assertEqual(M.get_height(), 3)


    def test_matrix_multiplication(self):
        A = matrix.SquareMatrix(3, [[1, 2, 3], [2, 2, 2], [3, 3, 3]])
        B = matrix.SquareMatrix(3, [[4, 4, 4], [5, 6, 7], [6, 6, 6]])
        C = matrix.SquareMatrix.multiplicate(A, B)
        self.assertEqual(C.data, [[32, 34, 36], [30, 32, 34], [45, 48, 51]])

    def test_lower_zero_triangle(self):
        A = matrix.SquareMatrix(3, [[1, 2, 3], [2, 2, 2], [4, 3, 3]])
        A.make_zeros_below_diagonal()
        self.assertEqual(A.data, [[1, 2, 3,], [0, -2, -4], [0, 0, 1]])


    def test_upper_zero_triangle(self):
        A = matrix.SquareMatrix(3, [[1, 2, 3], [1, 3, 2], [4, 3, 3]])
        print(A)

        # TODO: ova funkcija, je implementirana samo na sqm
        # TODO: pomerite njenu implementaciju na matricu
        # TODO: po uradjenom poslu. brisite je iz squer matrice i moraju svi testovi
        # TODO: da prodju

        A.make_upper_zero_triangle()
        print(A)

    def test_invert(self):

        A = matrix.SquareMatrix(3, [[1, 2, 7], [3, 2, 5], [1, 5, 2]])
        B = matrix.SquareMatrix(3, [[1, 2, 7], [3, 2, 5], [1, 5, 2]])

        print(A)
        A.invert()

        print(A)

        C = matrix.Matrix.multiplicate(A, B)

        print(C)

    def test_invert2(self):

        A = matrix.SquareMatrix(4, [[1, 2, 7, 1], [3, 2, 2, 5], [1, 11, 5, 2], [5, 21, 5, 1]])
        B = matrix.SquareMatrix(4, [[1, 2, 7, 1], [3, 2, 2, 5], [1, 11, 5, 2], [5, 21, 5, 1]])

        print(A)
        A.invert()

        print(A)

        C = matrix.Matrix.multiplicate(A, B)

        print(C)

    def test_invert3_stress(self):

        #NOTE: u testu nikada ne sme da se koristi rand funkcija

        import random

        dim = 10

        data = []
        data2 = []
        for row in range(dim):
            r = [random.randint(0,100) for _ in range(dim)]
            data.append(r)
            data2.append(r[:])

        A = matrix.SquareMatrix(dim, data=data)
        B = matrix.SquareMatrix(dim, data=data2)

        print(A)

        A.invert()

        print(A)

        C = matrix.Matrix.multiplicate(A, B)

        print(C)


        # print(A)
        # A.invert()
        #
        # print(A)
        #
        # C = matrix.Matrix.multiplicate(A, B)
        #
        # print(C)