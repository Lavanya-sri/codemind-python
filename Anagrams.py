a=input()
b=input()
x=a.lower()
y=b.lower()
if len(x)==len(y):
    c=sorted(x)
    d=sorted(y)
    if c==d:
        print("True")
    else:
        print("False")
else:
    print("False")