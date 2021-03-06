# encoding: utf-8

import unittest
import jokenpo

class TestJokenpo(unittest.TestCase):

    def test_j2_venceu_com_papel(self):
        jogador2 = "papel"
        resultado = jokenpo.jogo("spock", jogador2)
        resultado_esperado = "Jogador 2 venceu"
        self.assertEqual(resultado_esperado, resultado)
        resultado = jokenpo.jogo("pedra", jogador2)
        self.assertEqual(resultado_esperado, resultado)

    def test_j2_venceu_com_pedra(self):
        jogador2 = "pedra"
        resultado = jokenpo.jogo("tesoura", jogador2)
        resultado_esperado = "Jogador 2 venceu"
        self.assertEqual(resultado_esperado, resultado)
        resultado = jokenpo.jogo("lagarto", jogador2)
        self.assertEqual(resultado_esperado, resultado)

    def test_j2_venceu_com_tesoura(self):
        jogador2 = 'tesoura'
        resultado = jokenpo.jogo("papel", jogador2)
        resultado_esperado = 'Jogador 2 venceu'
        self.assertEqual(resultado_esperado,resultado)
        resultado = jokenpo.jogo("lagarto", jogador2)
        self.assertEqual(resultado_esperado,resultado)

    def test_j2_venceu_com_spock(self):
        jogador2 = "spock"
        resultado = jokenpo.jogo("pedra", jogador2)
        resultado_esperado = "Jogador 2 venceu"
        self.assertEqual(resultado_esperado, resultado)
        resultado = jokenpo.jogo("tesoura", jogador2)
        self.assertEqual(resultado_esperado, resultado)

    def test_j2_venceu_com_lagarto(self):
        jogador2 = 'lagarto'
        resultado = jokenpo.jogo("spock", jogador2)
        resultado_esperado = 'Jogador 2 venceu'
        self.assertEqual(resultado_esperado,resultado)
        resultado = jokenpo.jogo("papel", jogador2)
        self.assertEqual(resultado_esperado,resultado)



    def test_j1_venceu_com_tesoura(self):
        jogador1 = "tesoura"
        resultado = jokenpo.jogo(jogador1, "papel")
        resultado_esperado = "Jogador 1 venceu"
        self.assertEqual(resultado_esperado, resultado)
        resultado = jokenpo.jogo(jogador1, "lagarto")
        self.assertEqual(resultado_esperado, resultado)

    def test_empatepapel(self):
        jogador1 = "papel"
        jogador2 = "papel"
        resultado = jokenpo.jogo(jogador1, jogador2)
        resultado_esperado = "Jogadores empataram"
        self.assertEqual(resultado_esperado, resultado)
        jogador1 = "pedra"
        jogador2 = "pedra"
        resultado = jokenpo.jogo(jogador1, jogador2)
        self.assertEqual(resultado_esperado, resultado)
        jogador1 = "tesoura"
        jogador2 = "tesoura"
        resultado = jokenpo.jogo(jogador1, jogador2)
        self.assertEqual(resultado_esperado, resultado)
        jogador1 = "spock"
        jogador2 = "spock"
        resultado = jokenpo.jogo(jogador1, jogador2)
        self.assertEqual(resultado_esperado, resultado)
        jogador1 = "lagarto"
        jogador2 = "lagarto"
        resultado = jokenpo.jogo(jogador1, jogador2)
        self.assertEqual(resultado_esperado, resultado)

    def test_j1_venceu_com_pedra(self):
        jogador1 = "pedra"
        resultado = jokenpo.jogo(jogador1, "tesoura")
        resultado_esperado = "Jogador 1 venceu"
        self.assertEqual(resultado_esperado, resultado)
        resultado = jokenpo.jogo(jogador1, "lagarto")
        self.assertEqual(resultado_esperado, resultado)

    def test_j1_venceu_com_papel(self):
        jogador1 = "papel"
        resultado = jokenpo.jogo(jogador1, "spock")
        resultado_esperado = "Jogador 1 venceu"
        self.assertEqual(resultado_esperado, resultado)
        resultado = jokenpo.jogo(jogador1, "pedra")
        self.assertEqual(resultado_esperado, resultado)

    def test_j1_venceu_com_spock(self):
        jogador1 = "spock"
        resultado = jokenpo.jogo(jogador1, "tesoura")
        resultado_esperado = "Jogador 1 venceu"
        self.assertEqual(resultado_esperado, resultado)
        resultado = jokenpo.jogo(jogador1, "pedra")
        self.assertEqual(resultado_esperado, resultado)

    def test_j1_venceu_com_lagarto(self):
        jogador1 = "lagarto"
        resultado = jokenpo.jogo(jogador1, "spock")
        resultado_esperado = "Jogador 1 venceu"
        self.assertEqual(resultado_esperado, resultado)
        resultado = jokenpo.jogo(jogador1, "papel")
        self.assertEqual(resultado_esperado, resultado)


if __name__ == '__main__':
    unittest.main()