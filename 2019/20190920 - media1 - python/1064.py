

somaTotal = 0
contadorPositivos = 0

for i in range(6):
    n = float(input())
    if n > 0:

        contadorPositivos += 1
        somaTotal += n

print("{} valores positivos".format(contadorPositivos))
print("{:.1f}".format(somaTotal/contadorPositivos))

