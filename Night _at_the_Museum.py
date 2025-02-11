name=input()
name.lower()
letter='abcdefghijklmnopqrstuvwxyz'
pointer="a"
count=0
for i in range(len(name)):
    if pointer!=name[i]:
        length=abs(letter.index(pointer)-letter.index(name[i]))
        if length <= 13:
            count+=length
            pointer=name[i]
        else:
            length=26-length
            count+=length
            pointer=name[i]
print(count)
