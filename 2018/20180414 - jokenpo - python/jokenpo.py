# encoding: utf-8

def jogo(jogador1, jogador2):
    ganhador = 0
    if(jogador1 == jogador2): return 'Jogadores empataram'

    if(jogador1 == 'pedra'):
        if(jogador2 == 'papel'):
            ganhador = 2
        else:
            ganhador = 1

    if (jogador1 == 'tesoura'):
        if (jogador2 == 'pedra'):
            ganhador = 2
        else:
            ganhador = 1

    if (jogador1 == 'spock'):
        if (jogador2 == 'papel' or jogador2 == "lagarto"):
            ganhador = 2
        else:
            ganhador = 1

    if (jogador1 == 'papel'):
        if (jogador2 == 'tesoura' or jogador2 == 'spock'):
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