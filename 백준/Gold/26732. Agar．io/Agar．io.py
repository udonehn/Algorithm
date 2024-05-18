import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()


def solve(N, arr):
    arr = deque(sorted(arr))
    biggest = arr[-1]
    size = 2
    eatable = []
    count = 0
    while size < biggest:
        while arr and size > arr[0]:
            eatable.append(arr.popleft())
        if not eatable:
            return "NIE"
        size += eatable.pop()
        count += 1
    return count


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))

    print(solve(N, arr))
