import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()


def solve(N, K, T, arr):
    if sum(arr) % K != 0:
        return "NO"

    arr.sort()
    while arr[-1] > K:
        arr[-1] -= K
        arr.sort()
    arr = deque(arr)
    while arr and arr[0] == 0:
        arr.popleft()

    chance = T
    while arr:
        if K - arr[-1] > chance:
            return "NO"
        if arr[0] + arr[-1] == K:
            chance -= arr[0]
            arr.pop()
            arr.popleft()
        elif arr[0] + arr[-1] > K:
            arr[0] -= K - arr[-1]
            chance -= K - arr[-1]
            arr.pop()
        elif arr[0] + arr[-1] < K:
            arr[-1] += arr[0]
            chance -= arr[0]
            arr.popleft()
    return "YES"


if __name__ == "__main__":
    N, K, T = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(N, K, T, arr))

