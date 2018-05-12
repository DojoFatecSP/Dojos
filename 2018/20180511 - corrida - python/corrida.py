def fim_corrida(numero_de_carros, numero_de_voltas, lista_tempos):
    tempos = []
    resultado = []
    for carro in lista_tempos:
        tempos.append(sum(carro))
    copia = tempos[:]
    for t in range(3):
        resultado.append(tempos.index(min(copia))+1)
        copia.remove(min(copia))
    return resultado
