import sys
input = lambda: sys.stdin.readline().rstrip()


def solve(N, arr):
    arr.sort()
    result = 0
    for num in arr:
        if result + 1 < num:
            return result + 1
        result += num
    return result + 1

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    print(solve(N, arr))