import sys
input = lambda: sys.stdin.readline().rstrip()


def solve(N, arr):
    count = 0
    for i in range(N):
        if arr[i] - 1 == i:
            count += 1
            arr[i] = (i+1) % N + 1
    print(count)
    print(*arr)

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))

    solve(N, arr)