# encoding: utf-8

def jogador1venceu(i1, i2):
    if (i1 < i2):
        return (i1 % 2 != i2 % 2)
    else:
        return (i1 % 2 == i2 % 2)
            

def jogo(jogador1, jogador2):
    dic = {'tesoura': 1, "papel": 2, "pedra": 3, "lagarto": 4, "spock": 5}

    if(jogador1 == jogador2): return 'Jogadores empataram'

    if (jogador1venceu(dic[jogador1], dic[jogador2])):
        return "Jogador 1 venceu"
    else:
        return "Jogador 2 venceu"