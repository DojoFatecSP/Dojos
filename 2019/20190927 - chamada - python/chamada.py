a,b=map(int,input().split())
list=[]
for i in range (a):
    v=input()
    list.append(v)
list.sort()
print(list[b-1])