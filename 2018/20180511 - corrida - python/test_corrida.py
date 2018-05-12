import corrida
import unittest

class TestCorrida(unittest.TestCase):
    def test_corrida_um(self):
        carros = 3
        voltas = 1
        lista_tempos = [[1],[2],[3]]
        resultado_esperado = [1,2,3]
        resultado = corrida.fim_corrida(carros, voltas, lista_tempos)
        self.assertEqual(resultado_esperado, resultado)
    def test_corrida_dois(self):
        carros = 3
        voltas = 1
        lista_tempos = [[4],[5],[6]]
        resultado_esperado = [1,2,3]
        resultado = corrida.fim_corrida(carros, voltas, lista_tempos)
        self.assertEqual(resultado_esperado, resultado)

    def test_corrida_tres(self):
        carros = 3
        voltas = 2
        lista_tempos = [[1,2],[2,2],[2,3]]
        resultado_esperado = [1,2,3]
        resultado = corrida.fim_corrida(carros, voltas, lista_tempos)
        self.assertEqual(resultado_esperado, resultado)

    def test_corrida_quatro(self):
        carros = 3
        voltas = 2
        lista_tempos = [[2,2],[1,2],[2,3]]
        resultado_esperado = [2,1,3]
        resultado = corrida.fim_corrida(carros, voltas, lista_tempos)
        self.assertEqual(resultado_esperado, resultado)
if __name__ == '__main__':
    unittest.main()