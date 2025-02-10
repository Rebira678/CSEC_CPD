n=int(input())
listt=[]
count=1
for i in range(n):
    k=input()
    listt.append(k)
for i in range(1,len(listt)):
    if listt[i]!=listt[i-1]:
        count+=1
print(count)
