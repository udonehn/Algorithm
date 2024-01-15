def solve(N):
    dp=[1, 2]
    for i in range(2, N):
        dp.append((dp[i-1]+dp[i-2])%15746)

    return dp[N-1]%15746


if __name__ == "__main__":
    N = int(input())
    print(solve(N))