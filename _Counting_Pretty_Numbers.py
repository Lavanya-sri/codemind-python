t=int(input())
for i in range(t):
    l,r=map(int,input().split())
    count=0
    for i in range(l,r+1):
        a=str(i)
        if '2' in a[-1] or '3' in a[-1] or '9' in a[-1]:
            count+=1
    print(count)