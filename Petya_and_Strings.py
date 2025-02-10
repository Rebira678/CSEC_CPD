first=input()
second=input()
fir=first.lower()
sec=second.lower()
if fir < sec:
    print("-1")
elif sec < fir:
    print("1")
else:
    print("0")
