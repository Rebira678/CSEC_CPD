n=int(input())
just=[]
first=[]
second=[]
count=0
for i in range(n):
    take=map(int,input().split())
    for j in take:
        just.append(j)
for i in range(n*2):
    if i%2==0:
        first.append(just[i])
    else:
        second.append(just[i])
for i in range(n):
    for j in second:
        if j==first[i]:
            count+=1
print(count)
