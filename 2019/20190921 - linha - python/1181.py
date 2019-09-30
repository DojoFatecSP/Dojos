linha = [0]*12

L =int(input())
T = str(input())

for i in range(12*L):
    float(input())

for i in range(12):
    linha[i] = float(input())

result = sum(linha)

if T == "M":
    result = result/12

print("{:.1f}".format(result))
