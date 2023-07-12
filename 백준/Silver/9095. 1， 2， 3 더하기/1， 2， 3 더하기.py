arr=[]
dp=[1,2,4]
for _ in range(int(input())):
    arr.append(int(input()))
m=max(arr)
for i in range(4,m+1):
    dp.append(dp[i-4]+dp[i-3]+dp[i-2])
for i in arr:
    print(dp[i-1])