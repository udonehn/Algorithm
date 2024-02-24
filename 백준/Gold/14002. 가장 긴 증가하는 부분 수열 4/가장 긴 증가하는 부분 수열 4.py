if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    dp = [[arr[i]] for i in range(N)]
    for i in range(1, N):
        max_length = -1
        dp.append([])
        for j in range(i):
            if arr[i] > arr[j]:
                if len(dp[j]) > max_length:
                    max_length = len(dp[j])
                    dp[i] = dp[j]+[arr[i]]

    index=-1
    dp_max_length=-1
    for i in range(N):
        if len(dp[i])>dp_max_length:
            dp_max_length=len(dp[i])
            index=i
    print(len(dp[index]))
    print(*dp[index])

