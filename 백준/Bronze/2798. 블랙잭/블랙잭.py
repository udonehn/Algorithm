N, M =map(int, input().split())
arr=list(map(int,input().split()))
max=0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            sum=arr[i]+arr[j]+arr[k]
            if max<sum and sum<=M:
                max=sum
print(max)