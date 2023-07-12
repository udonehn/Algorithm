from collections import deque

N, M = map(int, input().split())
queue=deque([(N,1)])
ans=-1
while queue:
    X,count=queue.popleft()
    if X==M:
        ans=count
    if X>M:
        continue
    queue.append([X*2,count+1])
    queue.append([int(str(X)+'1'),count+1])
print(ans)