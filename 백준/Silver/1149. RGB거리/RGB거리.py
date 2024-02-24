import sys
input = lambda: sys.stdin.readline().rstrip()


def solve(N, arr):
    dp = [[arr[0][0], arr[0][1], arr[0][2]]]
    for i in range(1, N):
        dp.append([0, 0, 0])
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + arr[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + arr[i][1]
        dp[i][2] = min(dp[i - 1][1], dp[i - 1][0]) + arr[i][2]
    return min(dp[N-1])

if __name__ == "__main__":
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    print(solve(N, arr))
