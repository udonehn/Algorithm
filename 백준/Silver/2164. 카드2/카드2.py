import sys
from collections import deque

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(i+1)

queue = deque(arr)

while(len(queue)!=1):
    queue.popleft()
    a = queue.popleft()
    queue.append(a)

print(queue[0])