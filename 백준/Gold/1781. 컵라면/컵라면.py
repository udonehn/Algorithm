import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()


def solve(N, arr):
    arr.sort(key=lambda x: (x[0], -x[1]))
    selected = []
    for question in arr:
        d, c = question
        if d > len(selected):
            heappush(selected, c)
        elif selected[0] < c:
            heappop(selected)
            heappush(selected, c)
    return sum(selected)


if __name__ == "__main__":
    N = int(input())
    arr = []
    for _ in range(N):
        d, c = map(int, input().split())
        arr.append((d, c))
    print(solve(N, arr))
