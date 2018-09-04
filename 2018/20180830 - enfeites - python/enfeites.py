def solve(bolinhas):
    caixinhas = {}
    for bolinha in bolinhas:
        caixinhas[bolinha[0]] = []

    for bolinha in bolinhas:
        caixinhas[bolinha[0]].append(bolinha[1])
        #caixinhas[bolinha[0]].sort()

    for caixinha, bolas in caixinhas.items():
        bolas.sort(reverse=True)

    chaves = sorted(list(caixinhas.keys()))

    resultado = []

    for caixa in chaves:
        resultado = resultado + caixinhas[caixa]


    return resultado
