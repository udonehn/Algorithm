import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()


def solve(N, arr):
    queue = deque()
    for command in arr:
        if len(command) == 2:
            c, n = command
        else:
            c = command[0]

        if c == "push":
            queue.append(n)
        elif c == "pop":
            if not queue:
                print(-1)
            else:
                print(queue.popleft())
        elif c == "size":
            print(len(queue))
        elif c == "empty":
            if queue:
                print(0)
            else:
                print(1)
        elif c == "front":
            if not queue:
                print(-1)
            else:
                print(queue[0])
        elif c == "back":
            if not queue:
                print(-1)
            else:
                print(queue[-1])


if __name__ == "__main__":
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(input().split())

    solve(N, arr)
