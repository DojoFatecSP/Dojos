while True:
    linha = input().split()
    l = int(linha[0])
    r = int(linha[1])
    if r == 0 and l == 0:
        break
    print(l + r)