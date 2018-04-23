# encoding: utf-8

import unittest
import jokenpo

class TestJokenpo(unittest.TestCase):

    def test_jogador2venceuspock(self):
        jogador1 = "spock"
        jogador2 = "papel"
        resultado = jokenpo.jogo(jogador1, jogador2)
        resultado_esperado = "Jogador 2 venceu"
        self.assertEqual(resultado_esperado, resultado)

    def test_jogador2venceulagarto(self):
        jogador1 = "lagarto"
        jogador2 = "pedra"
        resultado = jokenpo.jogo(jogador1, jogador2)
        resultado_esperado = "Jogador 2 venceu"
        self.assertEqual(resultado_esperado, resultado)

    def test_jogador2venceutesoura(self):
        jogador1 = 'papel'
        jogador2 = 'tesoura'
        resultado = jokenpo.jogo(jogador1, jogador2)
        resultado_esperado = 'Jogador 2 venceu'
        self.assertEqual(resultado_esperado,resultado)

    def test_jogador2venceupapel(self):
        jogador1 = "pedra"
        jogador2 = "papel"
        resultado = jokenpo.jogo(jogador1, jogador2)
        resultado_esperado = "Jogador 2 venceu"
        self.assertEqual(resultado_esperado, resultado)


    def test_jogador2venceupedra(self):
        jogador1 = 'tesoura'
        jogador2 = 'pedra'
        resultado = jokenpo.jogo(jogador1, jogador2)
        resultado_esperado = 'Jogador 2 venceu'
        self.assertEqual(resultado_esperado,resultado)

    def test_jogador1venceutesoura(self):
        jogador1 = "tesoura"
        jogador2 = "papel"
        resultado = jokenpo.jogo(jogador1, jogador2)
        resultado_esperado = "Jogador 1 venceu"
        self.assertEqual(resultado_esperado, resultado)

    def test_empatepapel(self):
        jogador1 = "papel"
        jogador2 = "papel"
        resultado = jokenpo.jogo(jogador1, jogador2)
        resultado_esperado = "Jogadores empataram"
        self.assertEqual(resultado_esperado, resultado)

    def test_empatepedra(self):
        jogador1 = "pedra"
        resultado_esperado = "Jogadores empataram"
        jogador2 = "pedra"
        resultado = jokenpo.jogo(jogador1, jogador2)
        self.assertEqual(resultado_esperado, resultado)

    def test_empatetesoura(self):
        jogador1 = "tesoura"
        resultado_esperado = "Jogadores empataram"
        jogador2 = "tesoura"
        resultado = jokenpo.jogo(jogador1, jogador2)
        self.assertEqual(resultado_esperado, resultado)

    def test_jogador1venceupedra(self):
        jogador1 = "pedra"
        jogador2 = "tesoura"
        resultado = jokenpo.jogo(jogador1, jogador2)
        resultado_esperado = "Jogador 1 venceu"
        self.assertEqual(resultado_esperado, resultado)

    def test_jogador1venceupapel(self):
        jogador1 = "papel"
        jogador2 = "pedra"
        resultado = jokenpo.jogo(jogador1, jogador2)
        resultado_esperado = "Jogador 1 venceu"
        self.assertEqual(resultado_esperado, resultado)



unittest.main()