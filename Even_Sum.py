n=int(input())
arr=list(map(int,input().split()))
even=0
odd=0
for i in range(len(arr)):
    if arr[i]%2==0:
        even+=arr[i]
    else:
        odd+=arr[i]
print(even)