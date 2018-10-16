import unittest
import enfeites

class TesteEnfeite(unittest.TestCase):
    def test1(self):
        numero_de_bolinas = 2
        lista_de_bolinas = [
            [1, 1000],
            [1, 2000]
        ]
        resultado = [2000, 1000]
        self.assertEqual(enfeites.solve(lista_de_bolinas), resultado)

    def test2(self):
        numero_de_bolinas = 3
        lista_de_bolinas = [
            [1, 1000],
            [1, 2000],
            [1, 3000]
        ]
        resultado = [3000, 2000, 1000]
        self.assertEqual(enfeites.solve(lista_de_bolinas), resultado)


if __name__ == '__main__':
    unittest.main()