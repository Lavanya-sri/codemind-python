n=int(input())
a=0
b=1
n3=0
print(a,end=" ")
print(b,end=" ")
for i in range(2,n):
    n3=a+b
    print(n3,end=" ")
    a=b
    b=n3
       