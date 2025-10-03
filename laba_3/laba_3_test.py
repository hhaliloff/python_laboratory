from laba_3 import gen_bin_tree
import unittest


class TestMySolution(unittest.TestCase):

  def test_simple(self):
    self.assertEqual(gen_bin_tree(0, 0), {0: {}})
    # проверка дерева с корнем 0 и с высотой 0
    self.assertEqual(gen_bin_tree(3, 0), {3: {}})
    # проверка дерева с корнем не 0, но с высотой 0
    self.assertEqual(gen_bin_tree(0, 2), {0: {0: {0: {}, 4: {}}, 4: {8: {}, 12: {}}}})
    # проверка дерева с корнем 0 и с высотой 2
    self.assertEqual(gen_bin_tree(-1, 0), {-1: {}})
    # проверка дерева с отрицательным корнем и высотой 0
    self.assertEqual(gen_bin_tree(-1, 2), {-1: {-3: {-9: {}, 1: {}}, 3: {9: {}, 7: {}}}})
    # проверка дерева с отрицательным корнем и ненулевой высотой


if __name__ == '__main__':
  unittest.main()