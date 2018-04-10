# encoding: utf-8

def jogo(jogador1, jogador2):
    if jogador1 == 'tesoura' and jogador2 == "papel":
        return "Jogador 1 venceu"
    if jogador1 == "pedra" and jogador2 == "tesoura":
        return "Jogador 1 venceu"
    if jogador1 == "papel" and jogador2 == "pedra":
        return "Jogador 1 venceu"
    if jogador1 == "tesoura" and jogador2 == "pedra":
        return "Jogador 2 venceu"
    if jogador1 == "pedra" and jogador2 == "papel":
        return "Jogador 2 venceu"
    if jogador1 =" pedra"= jogador2:"pedra"
        return "Jogador empatados"
   if jogador1 ="papel"= jogador2:"papel"
        return "Jogador empatados"