def organizar_lista(jogadores,indice_jogador_inicial):
    jogadores= jogadores[indice_jogador_inicial:] + jogadores[:indice_jogador_inicial]
    return jogadores

def solve(q, f, a):
    chutes = 2 * f
    jogadores = list(range(q))
    jogadores.reverse()
    indice_jogador_inicial = jogadores.index(a)

    while len(jogadores) != 1: # enquanto numero de jogadores não for 1
        jogadores = organizar_lista(jogadores, indice_jogador_inicial)
        indice_eliminado= chutes%len(jogadores)   # calcular o aluno eliminado ********
        jogadores.pop(indice_eliminado)
        indice_jogador_inicial = indice_eliminado - 1
        chutes += 2


    # enquanto o indice do aluno inicial não for o indice final, add 1 no indice do aluno inicial. Quando chega no final,
    # indice do aluno inicial = 0
    # retirar o eliminado da lista
    # iniciar o calculo do jogador inicial a partir do indice do eliminado - 1
    # aumentar o chutes em 2




    return jogadores[0]