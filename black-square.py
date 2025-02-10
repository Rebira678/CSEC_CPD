n=map(int,input().split())
just=[]
total=0
for i in n:
    just.append(i)
take=input()
for i in take:
    total+=just[int(i)-1]
print(total)
