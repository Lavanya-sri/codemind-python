n=int(input())
x=n
add=0
for i in range(1,n):
    if n%i==0:
        add=add+i
if add==x:
    print("True")
else:
    print("False")