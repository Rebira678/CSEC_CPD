n = int(input())
birds = [0] + list(map(int, input().split()))
m = int(input())
for i in range(m):
    w, s = map(int, input().split())
    pointer = birds[w]
    count = s - 1
    count2 = pointer - s
    if w == 1:
        if w + 1 <= n:
            birds[w + 1] += count2
    elif w == n:
        if w - 1 >= 1:
            birds[w - 1] += count
    else:
        if w - 1 >= 1:
            birds[w - 1] += count
        if w + 1 <= n:
            birds[w + 1] += count2       
    birds[w] = 0
for i in range(1, n+1):
    print(birds[i])
