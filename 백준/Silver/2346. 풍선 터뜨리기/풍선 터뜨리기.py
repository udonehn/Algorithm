import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()


def solve(N, arr):
    queue = deque()
    for i in range(N):
        queue.append((i, arr[i]))
    answer = []
    while True:
        index, value = queue.popleft()
        answer.append(index+1)
        if not queue:
            return answer
        if value > 0:
            for _ in range(value-1):
                queue.append(queue.popleft())
        else:
            for _ in range(-value):
                queue.appendleft(queue.pop())


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    print(*solve(N, arr))
