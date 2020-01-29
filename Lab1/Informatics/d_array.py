a=int(input())
cnt=0
arr = input().split()
for i in range(len(arr)):
    arr[i] = int(arr[i])
for i in range(len(arr)-1):
    if(arr[i+1]>arr[i]):
        cnt+=1

print(cnt)
