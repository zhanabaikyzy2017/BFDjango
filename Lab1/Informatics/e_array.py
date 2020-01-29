a=int(input())
cnt=0
arr = input().split()
for i in range(len(arr)):
    arr[i] = int(arr[i])
for i in range(len(arr)-1):
    if(((arr[i+1]> 0) and (arr[i]>0)) or (arr[i+1]< 0 and arr[i]<0)):
        print("YES")
    else:
        print("NO")
