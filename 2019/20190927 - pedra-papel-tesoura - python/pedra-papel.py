ganhas ={"tesoura": ["lagarto", "papel"],
         "spock": ["tesoura", "pedra"],
         "lagarto": ["spock", "papel"],
         "papel": ["pedra", "spock"],
         "pedra": ["lagarto", "tesoura"]}

n = int(input())

for i in range(n):
    jog1, jog2 = input().split()
    if jog1 == jog2:
        print("empate")
    elif jog2 in ganhas[jog1]:
        print("rajesh")
    else:
        print("sheldon")
