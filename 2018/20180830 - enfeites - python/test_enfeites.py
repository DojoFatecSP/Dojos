import unittest
import enfeites

class TestEnfeites(unittest.TestCase):    
    def test_uma_bolinha(self):
        entrada = [[2, 10001]]
        saida = [10001]
        self.assertEqual(enfeites.solve(entrada), saida)

    def test_duas_bolinha(self):
        entrada = [[2, 10001], [2, 90090]]
        saida = [90090, 10001]
        self.assertEqual(enfeites.solve(entrada), saida)

    def test_duas_caixinhas(self):
        entrada = [[2, 10001], [2, 90090], [7, 75655], [7, 10032], [2, 70005]]
        saida = [90090, 70005, 10001, 75655, 10032]
        self.assertEqual(enfeites.solve(entrada), saida)

    def test_sete_bolinhas(self):
        entrada = [[2, 10001],
                    [2, 90090],
                    [4, 70007],
                    [3, 44444],
                    [2, 80008],
                    [4, 50005],
                    [3, 20022]]
        saida = [90090,
                 80008,
                 10001,
                 44444,
                 20022,
                 70007,
                 50005]
        self.assertEqual(enfeites.solve(entrada), saida)

    def test_last_ultimate(self):
        entrada = [
            [4, 98622],
            [9, 91],
            [9, 911],
            [5, 387],
            [9, 376],
            [10, 3],
            [1, 1505],
            [4, 14],
            [6, 102],
            [9, 105]]
        saida =[
        1505,
        98622,
        14,
        387,
        102,
        911,
        376,
        105,
        91,
        3]
        self.assertEqual(enfeites.solve(entrada), saida)

if __name__ == '__main__':
    unittest.main()