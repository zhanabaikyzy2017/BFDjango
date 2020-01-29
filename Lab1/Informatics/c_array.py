a=int(input())
cnt=0
arr = input().split()
for i in range(len(arr)):
    arr[i] = int(arr[i])
for i in range(len(arr)):
    if(arr[i]>0):
        cnt+=1

print(cnt)
