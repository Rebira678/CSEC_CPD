user_name=input()
name=user_name.lower()
count=len(set(name))
if count%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
