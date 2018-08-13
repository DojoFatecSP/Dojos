n = int(input())
lista_frequencias = [0] * 60

for i in range(n):
    anteriores = input().split()
    for numero in anteriores:
        lista_frequencias[int(numero) - 1] -= 1
indice_frequencias = []

for indice in range(60):
    freq = lista_frequencias[indice]
    indice_frequencias.append((freq, indice + 1))

indice_frequencias = sorted(indice_frequencias)
frequencias = input().split()
result = []
for f in frequencias:
    result.append(indice_frequencias[int(f) - 1][1])

print(*result)
