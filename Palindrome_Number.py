t=int(input())
add=0
while t>0:
    a=int(input())
    x=a
    add=0
    while a>0:
        r=a%10
        add=add*10+r
        a=a//10
    if x==add:
        print("True")
    else:
        print("False")
    t=t-1