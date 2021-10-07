import unittest
from Calculator import Calculator

class TestCalculator(unittest.TestCase):
  
  def setUp(self):
    self.calculator = Calculator()

    # Сложение
  def test_add(self):
    self.assertEqual(self.calculator.add(4,7), 11)

    # Вычитание
  def test_subtract(self):
    self.assertEqual(self.calculator.subtract(10,5), 5)

    # Умножение
  def test_multiply(self):
    self.assertEqual(self.calculator.multiply(3,7), 21)

    # Деление
  def test_divide(self):
    self.assertEqual(self.calculator.divide(10,2), 5)

if __name__ == "__main__":
  unittest.main()


