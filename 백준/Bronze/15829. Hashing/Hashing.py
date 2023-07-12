N=int(input())
arr=list(input())
ans=0
for i in range(N):
    ans+=(ord(arr[i])-96)*31**i
print(ans)