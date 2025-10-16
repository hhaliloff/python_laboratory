from .laba_2 import findnum
import unittest


class TestMySolution(unittest.TestCase):

  def test_simple(self):
    self.assertEqual(findnum([0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]), "Это число: 0")
    self.assertEqual(findnum([-3, [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]), "Это число: -3")
    # проверяем отрицательные числа вместе с положительными
    self.assertEqual(findnum([-5, [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]]), "Это число: -5")
    # проверяем только отрицательные числа
    self.assertEqual(findnum([0, [0]]), "Это число: 0")
    # проверяем диапазон с одним элементом
    self.assertEqual(findnum([0, [0, 1]]), "Это число: 0")
    # проверяем диапазон с двумя элементами
    self.assertEqual(findnum([-3, [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]), "Это число: -3")
    # проверяем нижнюю границу
    self.assertEqual(findnum([10, [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]), "Это число: 10")
    # проверяем верхнюю границу


if __name__ == '__main__':
  unittest.main()