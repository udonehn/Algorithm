from collections import deque
import sys

def BFS(graph, i):
    count=1
    queue=deque([i])
    visited=[False]*len(graph)
    visited[i]=True
    while queue:
        v=queue.popleft()
        for j in graph[v]:
            if not visited[j]:
                visited[j]=True
                queue.append(j)
                count+=1
    return count

N, M = map(int, sys.stdin.readline().split())

graph=[[] for _ in range(N+1)]

for _ in range(M):
    A,B=map(int, sys.stdin.readline().split())
    graph[B].append(A)
count=[-1]
for i in range(1,N+1):
    count.append(BFS(graph,i))
m=max(count)
for i in range(1,N+1):
    if count[i]==m:
        print(i,end=' ')