total=0
just=[]
count=0
n=int(input())
check=map(int,input().split())
for i in check:
    just.append(i)
for i in range(n):
    total+=just[i]
    if total == -1:
        count+=1
        total+=1
print(count)
