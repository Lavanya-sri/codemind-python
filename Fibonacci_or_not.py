n=int(input())
a=0
b=1
c=0
i=0
while True:
    c=a+b
    a,b=b,c
    i+=1
    if c==n:
        print("True")
        break
    else:
        if c>n:
            print("False")
            break