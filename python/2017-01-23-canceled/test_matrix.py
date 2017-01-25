import unittest

import mtx

class TestMatrica(unittest.TestCase):

    def test_matmul(self):

        A = mtx.Matrica(3, 1, [[1, 2, 3]])
        B = mtx.Matrica(1, 3, [[4], [5], [6]])
        C = mtx.Matrica.mnozenje_matrica(A, B)
        self.assertEqual(C.data, [[32]])

    def test_matmul_2(self):
        A = mtx.Matrica(3, 2, [[1, 2, 3], [4, 5, 6]])
        B = mtx.Matrica(3, 3, [[10, 20, 30], [15, 25, 35], [11, 22, 33]])
        C = mtx.Matrica.mnozenje_matrica(A, B)
        self.assertEqual(C.data, [[73, 136, 199], [181, 337, 493]])

    def test_matmul_3(self):
        A = mtx.Matrica(2, 4, [[1, 2], [3, 4], [5, 6], [7, 8]])
        B = mtx.Matrica(7, 2, [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])

        C = mtx.Matrica.mnozenje_matrica(A, B)
        self.assertEqual(C.data,[[17, 20, 23, 26, 29, 32, 35],
                          [35, 42, 49, 56, 63, 70, 77],
                          [53, 64, 75, 86, 97, 108, 119],
                          [71, 86, 101, 116, 131, 146, 161]])


    def test_matmul_4(self):
        A = mtx.Matrica(1, 3, [[4], [5], [6]])
        B = mtx.Matrica(3, 1, [[1, 2, 3]])
        C = mtx.Matrica.mnozenje_matrica(A, B)


    def test_matmul_fail(self):
        A = mtx.Matrica(1, 4, [[4], [5], [6], [7]])
        B = mtx.Matrica(3, 1, [[1, 2, 3]])
        with self.assertRaises(mtx.IzuzetakUlazniParametarDataNemaDobreDimenzije):
            C = mtx.Matrica.mnozenje_matrica(A, B)



if __name__ == '__main__':
     unittest.main()