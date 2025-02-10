total = 0
n, h = map(int, input().split())  
k = list(map(int, input().split()))  
for j in k:  
    if j > h:  
        result = 2  
    else:
        result = 1   
    total += result
print(total)
