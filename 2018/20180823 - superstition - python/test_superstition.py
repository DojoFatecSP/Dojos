import unittest
import superstition

class TestSuperstition(unittest.TestCase):
    def test1questao(self):
        questoes = 1
        resultado = 2
        self.assertEqual(resultado, superstition.calcula(questoes))

    def test2questoes(self):
        questoes = 2
        resultado = 3
        self.assertEqual(resultado, superstition.calcula(questoes))


if __name__ == "__main__":
    unittest.main()