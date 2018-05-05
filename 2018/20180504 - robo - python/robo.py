#coding:utf-8
numeroDePassos = int(input("Insira o número de passos: "))
entradas=[]

while(numeroDePassos>0):
    numeroDePassos -=1
    passo = raw_input("Digite o passo: ")
    if(passo == "E"):
        entradas.append(-1)
    elif(passo == "D"):
        entradas.append(1)
    else:
        batata = entradas[int(passo)-1]
        entradas.append(batata)
print(entradas)
print(sum(entradas))
