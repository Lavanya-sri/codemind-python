n=input()
s=input()
for i in n:
    if i==s:
        print("True")
        print(n.index(i))
        break
else:
    print("False")