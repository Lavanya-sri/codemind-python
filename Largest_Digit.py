n=int(input())
r=0
big=0
while n>0:
    r=n%10
    if r>big:
        big=r
    n=n//10
print(big)