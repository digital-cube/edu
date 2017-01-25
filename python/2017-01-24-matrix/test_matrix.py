
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

    # def test_gaus1(self):
    #
    #     A = matrix.Matrix(4, 5, [[2, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])
    #
    #     A.gaus1(0)
    #     print(A)
    #     A.gaus1(1)
    #     print(A)
    #     A.gaus1(2)
    #     print(A)


        # A = matrix.Matrix(4, 5, [[1, 2, 3, 4, 5], [0, 5, 8, 9, 10], [0, 12, 13, 14, 15], [0, 17, 18, 19, 20]])


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


