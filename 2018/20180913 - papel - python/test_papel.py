import papel
import unittest

class TestPapel(unittest.TestCase):
    def test1(self):
        quant_alunos = 2
        folhas = 1
        aluno_inicial = 0
        vencedor = 1
        resultado = papel.solve(quant_alunos, folhas, aluno_inicial)
        self.assertEqual(resultado, vencedor)

    def test2(self):
        quant_alunos = 2
        folhas = 2
        aluno_inicial = 0
        vencedor = 1
        resultado = papel.solve(quant_alunos, folhas, aluno_inicial)
        self.assertEqual(resultado,vencedor)

    def test3(self):
        quant_alunos = 5
        folhas = 1
        aluno_inicial = 4
        vencedor = 1
        resultado = papel.solve(quant_alunos, folhas, aluno_inicial)
        self.assertEqual(resultado,vencedor)

    def test4(self):
        quant_alunos = 2
        folhas = 5
        aluno_inicial = 1
        vencedor = 0
        resultado = papel.solve(quant_alunos, folhas, aluno_inicial)
        self.assertEqual(resultado,vencedor)

if __name__ == '__main__':
    unittest.main()