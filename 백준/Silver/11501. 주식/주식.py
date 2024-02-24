import sys
input = lambda: sys.stdin.readline().rstrip()


def solve(N, arr):
    result = 0
    arr.reverse()
    last = arr[0]
    for num in arr[1:]:
        if num <= last:
            result += last - num
        else:
            last = num
    return result


if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        print(solve(N, arr))