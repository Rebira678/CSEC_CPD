values=list(map(int,input().split()))
if values[0]<values[1]:
    result=values[1]
else:
    result=values[0]
result=7-result
if result==6:
    print("1/1")
elif result==5:
    print("5/6")
elif result==4:
    print("2/3")
elif result==3:
    print("1/2")
elif result==2:
    print("1/3")
else:
    print("1/6")
    
