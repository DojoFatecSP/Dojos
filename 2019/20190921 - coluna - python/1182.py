linha = [0]*12

C =int(input())
T = str(input())

coluna = []

for i in range(12):
    for j in range(12):
        n=float(input())
        if j == C:
            coluna.append(n)

result = sum(coluna)
if T == "M":
    result = result/12

print("{:.1f}".format(result))
