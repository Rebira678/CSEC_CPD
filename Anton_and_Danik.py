n = int(input())  
s = input().strip()
Anton = s.count('A')
Danik = s.count('D')
if Anton > Danik:
    print("Anton")
elif Danik > Anton:
    print("Danik")
else:
    print("Friendship")
