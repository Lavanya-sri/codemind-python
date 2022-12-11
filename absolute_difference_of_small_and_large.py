s=input()
s=s.split()
for words in s:
    x=max(words)
    y=min(words)
    z=abs(ord(x)-ord(y))
    print(z,end=" ")