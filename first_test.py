import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_calculat_correctly(self):
        assert self.calc.adding(self, 3, 3) == 6

    def test_subtraction_calculat_correctly(self):
        assert self.calc.subtraction(self, 9, 2) == 7

    def test_multiply_calculat_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calculat_correctly(self):
        assert self.calc.division(self, 10, 2) == 5




