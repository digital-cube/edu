from unittest import TestCase #1 iz unittest biblioteke koristimo TestCase klasu koju nasa klasa nasledjuje (Inheritance)
from  calc import Calc  #2 pozivamo klasu koju testiramo

class TestCalc(TestCase):
    def test_calculator_add(self):
        self.assertEqual(Calc().calculator(1, "+", 3), 4)

    def test_calculator_sub(self):
        self.    assertEqual(Calc().calculator(4, "-", 2), 2)

    def test_calculator_multiplication(self):
        self.assertEqual(Calc().calculator(5, "*", 2), 10)

    def test_calculator_division(self):
        self.assertEqual(Calc().calculator(50, "/", 5), 10)

    def test_invalid_operator(self):
        self.assertFalse(Calc().calculator(5, "j", 5))

    def test_invalid_operator_intiger(self):
        self.assertFalse(Calc().calculator(5, 0, 5))

    def test_invalid_operator_string_letter(self):
        self.assertFalse(Calc().calculator('i', "+", 5))

    def test_invalid_operator_string_number(self):
        self.assertEqual(Calc().calculator('1', "+", 5), 6)

    def test_invalid_operator_minus_string_number(self):
        self.assertEqual(Calc().calculator('-1', "+", 5), 4)

    def test_invalid_operator_float(self):
        self.assertEqual(Calc().calculator(1.5, "+", 5.2), 6.7)

    def test_division_zero(self):
        self.assertFalse(Calc().calculator('4', "/", 0))

    def test_invalid_operator_string_letter(self):
        self.assertEqual(Calc().calculator('1', "+", '4'), 5)