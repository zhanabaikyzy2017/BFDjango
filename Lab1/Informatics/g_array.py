a=int(input())
cnt=0
ans = ""

arr = input().split()
for i in range(len(arr)):
    arr[i] = int(arr[i])
for i in range(len(arr)-1 ,-1, -1 ):
    ans+= (str(arr[i]) + " ")

print(ans)
