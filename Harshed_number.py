n=int(input())
add=0
x=n
while n!=0:
    r=n%10
    add+=r
    n=n//10
if x%add==0:
    print("True")
else:
    print("False")