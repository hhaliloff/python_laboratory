from .laba_7 import get_currencies
import unittest
import requests


class TestMySolution(unittest.TestCase):

  def test_simple(self):
    self.assertEqual(get_currencies(["USD", "JPY", "AZN", "EUR"]), {'USD': 76.9708, 'JPY': 49.585, 'AZN': 45.2769, 'EUR': 89.9011})
    # проверяем соответствие курсам
    with self.assertRaises(KeyError):
        get_currencies(["USDT"])
    # проверяем поведение при несуществующей валюте
    with self.assertRaises(requests.exceptions.ConnectionError):
        get_currencies(["USD"], url = "https://thiswebsitedoesnotexist123456789.com")
    # проверяем поведение при несуществующей ссылке
    with self.assertRaises(ValueError):
        get_currencies(["USD"], url = "ht!tp://wrong_url")
    # проверяем поведение при ссылке с ошибкой


if __name__ == '__main__':
  unittest.main()