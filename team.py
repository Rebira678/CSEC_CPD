n=int(input())
count=0
for i in range(n):
    p,v,t=map(int,input().split())
    if p == v==1 or p == t==1 or v == t==1:
        count +=1
print(count)
