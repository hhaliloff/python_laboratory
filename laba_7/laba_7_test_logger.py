import unittest
from .laba_7 import solve_quadratic, io_file


class TestQuadraticLogger(unittest.TestCase):

    def test_solve_quadratic_logging(self):
        io_file.truncate(0)
        io_file.seek(0)

        x1, x2 = solve_quadratic(1, -3, 2)
        self.assertEqual((x1, x2), (2.0, 1.0))

        logs = io_file.getvalue()
        self.assertIn("INFO: starting function solve_quadratic", logs)
        self.assertIn("INFO: successfully finished function with result (2.0, 1.0)", logs)
        self.assertIn("INFO:quadratic:x1 = 2.0", logs)
        self.assertIn("INFO:quadratic:x2 = 1.0", logs)

        io_file.truncate(0)
        io_file.seek(0)

        with self.assertRaises(TypeError):
            solve_quadratic("abc", 1, 1)

        logs = io_file.getvalue()
        self.assertIn("INFO: starting function solve_quadratic", logs)
        self.assertIn("Error:", logs)
        self.assertIn("TypeError", logs)
        self.assertIn("ERROR:quadratic:Введите числовые значения для коэффициентов a, b и c", logs)

        io_file.truncate(0)
        io_file.seek(0)

        with self.assertRaises(ValueError):
            solve_quadratic(1, 0, 1)

        logs = io_file.getvalue()
        self.assertIn("INFO: starting function solve_quadratic", logs)
        self.assertIn("Error:", logs)
        self.assertIn("ValueError", logs)
        self.assertIn("WARNING:quadratic:Дискриминант меньше нуля, корней нет", logs)

        io_file.truncate(0)
        io_file.seek(0)

        with self.assertRaises(ValueError):
            solve_quadratic(0, 0, 1)

        logs = io_file.getvalue()
        self.assertIn("INFO: starting function solve_quadratic", logs)
        self.assertIn("Error:", logs)
        self.assertIn("ValueError", logs)
        self.assertIn("CRITICAL:quadratic:Коэффициенты a и b не могут быть равны нулю одновременно", logs)


if __name__ == "__main__":
    unittest.main()
