import sys
input = lambda: sys.stdin.readline().rstrip()


def solve(H, W, arr):
    result = 0
    for index in range(1, W-1):
        h = min(max(arr[:index]), max(arr[index+1:])) - arr[index]
        if h > 0:
            result += h
    return result


if __name__ == "__main__":
    H, W = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(H, W, arr))