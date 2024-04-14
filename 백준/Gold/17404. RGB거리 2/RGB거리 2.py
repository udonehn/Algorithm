import sys
input = lambda: sys.stdin.readline().rstrip()


def solve(N, rgb):
    answer = sys.maxsize
    for i in range(3):
        dp = [[sys.maxsize for _ in range(3)] for _ in range(N)]
        dp[0][i] = rgb[0][i]
        for j in range(1, N):
            dp[j][0] = rgb[j][0] + min(dp[j-1][1], dp[j-1][2])
            dp[j][1] = rgb[j][1] + min(dp[j-1][0], dp[j-1][2])
            dp[j][2] = rgb[j][2] + min(dp[j-1][0], dp[j-1][1])
        for j in range(3):
            if i == j:
                continue
            answer = min(answer, dp[-1][j])
    return answer


if __name__ == "__main__":
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    print(solve(N, arr))
