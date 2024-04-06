import sys
input = lambda: sys.stdin.readline().rstrip()


def solve(N, T, items):
    dp = [[0 for _ in range(T + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, T + 1):
            weight, value = items[i - 1]
            if j < weight:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
    return dp[N][T]


if __name__ == "__main__":
    N, T = map(int, input().split())
    question = []
    for _ in range(N):
        question.append(tuple(map(int, input().split())))
    print(solve(N, T, question))
