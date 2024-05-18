import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()


d = deque()
for _ in range(int(input())):
    command = list(map(int, input().split()))
    if command[0] == 1:
        d.appendleft(command[1])
    elif command[0] == 2:
        d.append(command[1])
    elif command[0] == 3:
        if not d:
            print(-1)
        else:
            print(d.popleft())
    elif command[0] == 4:
        if not d:
            print(-1)
        else:
            print(d.pop())
    elif command[0] == 5:
        print(len(d))
    elif command[0] == 6:
        if d:
            print(0)
        else:
            print(1)
    elif command[0] == 7:
        if d:
            print(d[0])
        else:
            print(-1)
    elif command[0] == 8:
        if d:
            print(d[-1])
        else:
            print(-1)
            