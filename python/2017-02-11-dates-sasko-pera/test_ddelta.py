from unittest import TestCase

import ddelta

class TestDdelta(TestCase):

    def setUp(self):
        pass

    def test_is_laep_year_2016(self):
        self.assertTrue(ddelta.is_leap_year(2016))

    def test_is_laep_year_2017(self):
        self.assertFalse(ddelta.is_leap_year(2017))

    def test_is_laep_year_2018(self):
        self.assertFalse(ddelta.is_leap_year(2018))

    def test_is_laep_year_2020(self):
        self.assertTrue(ddelta.is_leap_year(2020))

    def test_is_laep_year_1900(self):
        self.assertFalse(ddelta.is_leap_year(1900))

    def test_is_laep_year_2000(self):
        self.assertTrue(ddelta.is_leap_year(2000))

    def test_ddelta_same_date(self):
        self.assertEqual(0, ddelta.ddelta((2017, 2, 11), (2017, 2, 11)))

    def test_days_in_april_2017(self):
        self.assertEqual(30, ddelta.days_in_month(2017, 4))

    def test_days_in_january_2017(self):
        self.assertEqual(31, ddelta.days_in_month(2017, 1))

    def test_days_in_february_2017(self):
        self.assertEqual(28, ddelta.days_in_month(2017, 2))

    def test_days_in_february_2016(self):
        self.assertEqual(29, ddelta.days_in_month(2016, 2))

    def test_is_date_valid(self):
        self.assertTrue(ddelta.is_date_valid((2016, 2, 3)))
        self.assertTrue(ddelta.is_date_valid((2016, 2, 29)))
        self.assertFalse(ddelta.is_date_valid((2017, 2, 29)))
        self.assertFalse(ddelta.is_date_valid(("PERA", 2, 29)))
        self.assertFalse(ddelta.is_date_valid((2017, "2", 29)))
        self.assertFalse(ddelta.is_date_valid((2017, 2, "29")))

    def test_next_date(self):

        self.assertEqual((2017, 5, 3), ddelta.next_date((2017, 5, 2)))
        self.assertEqual((2017, 6, 1), ddelta.next_date((2017, 5, 31)))
        self.assertEqual((2019, 1, 1), ddelta.next_date((2018, 12, 31)))

    def test_ddelta_invalid_data_type(self):

        with self.assertRaises(ddelta.InvalidDataType):
            ddelta.ddelta("pera", "sasko")

        with self.assertRaises(ddelta.InvalidDataType):
            ddelta.ddelta((2017, 2, 11), "sasko")

        with self.assertRaises(ddelta.InvalidDataType):
            ddelta.ddelta((2017, 2, 11, 3), (2017, 2, 11))

        with self.assertRaises(ddelta.InvalidDataType):
            ddelta.ddelta((2017, 2, 11, 3), (2017, 2, 11, 3))

        with self.assertRaises(ddelta.InvalidDataType):
            ddelta.ddelta((2017, 22, 11), (2017, 32, 11))

        with self.assertRaises(ddelta.InvalidDataType):
            ddelta.ddelta((2017, 10, 35), (2017, 1, 1))

        with self.assertRaises(ddelta.InvalidDataType):
            ddelta.ddelta((2017, 10, 32), (2017, 1, 1))

        self.assertEqual(0, ddelta.ddelta((2017, 10, 31), (2017, 10, 31)))

        with self.assertRaises(ddelta.InvalidDataType):
            ddelta.ddelta((2017, 9, 31), (2017, 1, 1))

        with self.assertRaises(ddelta.InvalidDataType):
            ddelta.ddelta((2017, 2, 29), (2017, 1, 1))

        self.assertEqual(0, ddelta.ddelta((2016, 2, 29), (2016, 2, 29)))

        with self.assertRaises(ddelta.InvalidDataType):
            ddelta.ddelta((2017, 1, 1), (2017, 2, 29))

    def test_ddelta_2(self):

        self.assertEqual(0, ddelta.ddelta((2016, 2, 29), (2016, 2, 29)))
        self.assertEqual(1, ddelta.ddelta((2016, 1, 1), (2016, 1, 2)))
        self.assertEqual(2, ddelta.ddelta((2016, 1, 1), (2016, 1, 3)))
        self.assertEqual(3, ddelta.ddelta((2016, 1, 1), (2016, 1, 4)))
        self.assertEqual(4, ddelta.ddelta((2016, 1, 1), (2016, 1, 5)))
        self.assertEqual(5, ddelta.ddelta((2016, 1, 1), (2016, 1, 6)))
        self.assertEqual(36, ddelta.ddelta((2016, 1, 1), (2016, 2, 6)))

        self.assertEqual(15170, ddelta.ddelta((1975, 8, 1), (2017, 2, 11)))
        self.assertEqual(27705, ddelta.ddelta((1941, 4, 6), (2017, 2, 11)))
        self.assertEqual(21171, ddelta.ddelta((1941, 4, 6), (1999, 3, 24)))
        self.assertEqual(-21171, ddelta.ddelta((1999, 3, 24), (1941, 4, 6)))
        self.assertEqual(736370, ddelta.ddelta((1, 1, 1), (2017, 2, 11)))

