# encoding: utf-8

def jogador1venceu(i1, i2):
    if (i1 < i2):
        if (i1 % 2 != i2 % 2):
            return True
        else:
            return False

def jogador2venceu(i1, i2):
    if (i2 < i1):
        if (i1 % 2 == i2 % 2):
            return True
        else:
            return False

def jogo(jogador1, jogador2):
    dic = {'tesoura': 1, "papel": 2, "pedra": 3, "lagarto": 4, "spock": 5}

    """

    if jogador1venceu():
        return "Jogador 1 venceu"
    else:
        return "Jogador 2 venceu'
    """

    if(jogador1 == jogador2): return 'Jogadores empataram'

    if (jogador1venceu(dic[jogador1], dic[jogador2])):
        return "Jogador 1 venceu"

    if (jogador2venceu(dic[jogador1], dic[jogador2])):
        return "Jogador 2 venceu"

    if(jogador1 == 'pedra'):
        if(jogador2 == 'papel' or jogador2 == "spock"):
            ganhador = 2
        else:
            ganhador = 1

    if (jogador1 == 'tesoura'):
        if (jogador2 == 'pedra' or jogador2 == 'spock'):
            ganhador = 2
        else:
            ganhador = 1

    if (jogador1 == 'spock'):
        if (jogador2 == 'papel' or jogador2 == "lagarto"):
            ganhador = 2
        else:
            ganhador = 1

    if (jogador1 == 'papel'):
        if (jogador2 == 'tesoura' or jogador2 == 'lagarto'):
            ganhador = 2
        else:
            ganhador = 1

    if (jogador1 == 'lagarto'):
        if (jogador2 == 'tesoura' or jogador2 == 'pedra'):
            ganhador = 2
        else:
            ganhador = 1

    if(ganhador == 1):
        return 'Jogador 1 venceu'
    elif(ganhador == 2):
        return 'Jogador 2 venceu'
    else:
        return 'Erro'



    '''
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
    '''