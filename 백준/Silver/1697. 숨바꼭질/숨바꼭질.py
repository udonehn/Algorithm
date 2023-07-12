from collections import deque
import sys
input=lambda:sys.stdin.readline().rstrip()

N, K = map(int, input().split())
count=0
arr=set([N])
queue=deque([(N,count)])
while True:
    s,count=queue.popleft()
    if s==K:
        break
    n=s+1
    if n not in arr and 0<=n<=100000:
        queue.append((n,count+1))
        arr.add(n)
    n=s-1
    if n not in arr and 0<=n<=100000:
        queue.append((n,count+1))
        arr.add(n)
    n=s*2
    if n not in arr and 0<=n<=100000:
        queue.append((n,count+1))
        arr.add(n)
print(count)