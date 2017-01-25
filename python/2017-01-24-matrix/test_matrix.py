
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

    def tm2(self):
        '''
            generisati ove dve matrice

            https://www.dropbox.com/s/8443rhsjm0rszo4/Screenshot%202017-01-25%2010.35.17.png?dl=0

            pomnoziti i proveriti rezultat:

            https://www.dropbox.com/s/kyhm60o51o3vp70/Screenshot%202017-01-25%2010.36.10.png?dl=0
        '''


class TestSquareMatrix(unittest.TestCase):

    def test_constructor_width_and_height(self):
        M = matrix.SquareMatrix(3)
        self.assertEqual(M.get_dimension(), 3)
        self.assertEqual(M.get_width(), 3)
        self.assertEqual(M.get_height(), 3)



