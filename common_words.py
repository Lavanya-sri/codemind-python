s=input().lower().split()
t=input().lower().split()
if  len(s)>len(t):
    for words in s:
        if words in t:
            print(words,end=" ")
else:
    for words in t:
        if words in s:
            print(words,end=" ")