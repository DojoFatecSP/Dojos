import unittest
import frequencia

class TestFrequencia(unittest.TestCase):
    def test_1(self):
        self.assertEqual(frequencia.calcula(100, 76, 0),"soh um milagre")

    def test_2(self):
        self.assertEqual(frequencia.calcula(70, 10, 10),"sem chance")

    def test_3(self):
        self.assertEqual(frequencia.calcula(100, 10, 90),"tranquilo pode faltar 25 dias")

    def test_4(self):
        self.assertEqual(frequencia.calcula(100, 9, 90),"tranquilo pode faltar 24 dias")


if __name__ == "__main__":
    unittest.main()