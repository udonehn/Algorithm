import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
visited=[False]*(N+1)
graph=[[] for _ in range(N+1)]

for _ in range(M):
    A,B=map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

count=0

for i in range(N):
    if not visited[i+1]:
        queue=deque([i+1])
        while queue:
            v=queue.popleft()
            visited[v]=True
            for j in graph[v]:
                if not visited[j]:
                    visited[j]=True
                    queue.append(j)
        count+=1
        
print(count)