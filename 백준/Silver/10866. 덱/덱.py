import sys
from collections import deque
N = int(sys.stdin.readline())
deq = deque()
for _ in range(N):
    arr = sys.stdin.readline().strip().split()
    if arr[0]=='push_front':
        deq.appendleft(int(arr[1]))
    elif arr[0]=='push_back':
        deq.append(int(arr[1]))
    elif arr[0]=='pop_front':
        if len(deq)==0:
            print(-1)
        else:
            print(deq.popleft())
    elif arr[0]=='pop_back':
        if len(deq)==0:
            print(-1)
        else:
            print(deq.pop())
    elif arr[0]=='size':
        print(len(deq))
    elif arr[0]=='empty':
        if len(deq)==0:
            print(1)
        else:
            print(0)
    elif arr[0]=='front':
        if len(deq)==0:
            print(-1)
        else:
            print(deq[0])
    else:
        if len(deq)==0:
            print(-1)
        else:
            print(deq[-1])