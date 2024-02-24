if __name__ == "__main__":
    A = list(input())
    B = list(input())
    dp = [[0 for _ in range(len(A)+1)] for _ in range(len(B)+1)]

    for i in range(len(B)):
        for j in range(len(A)):
            if A[j] == B[i]:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

    print(dp[-1][-1])
