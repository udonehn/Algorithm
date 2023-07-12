from collections import deque

def DFS(graph,start,visited):
    visited[start]=True
    print(start,end=' ')
    for i in graph[start]:
        if not visited[i]:
            DFS(graph,i,visited)

def BFS(graph,start,visited):
    queue=deque([start])
    while queue:
        v=queue.popleft()
        visited[v]=True
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

N,M,V=map(int, input().split())
graph=[[]for _ in range(N+1)]

for _ in range(M):
    A,B=map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
    
for i in graph:
    i.sort()

visited=[False]*(N+1)
DFS(graph,V,visited)
print()
visited=[False]*(N+1)
BFS(graph,V,visited)