n=int(input())
r=0
x=n*n
add=0
while n>0:
    r=n%10
    add=add*10+r
    n=n//10
count=0
b=0
a=add*add
while a>0:
    b=a%10
    count=count*10+b
    a=a//10
if x==count:
    print("True")
else:
    print("False")
