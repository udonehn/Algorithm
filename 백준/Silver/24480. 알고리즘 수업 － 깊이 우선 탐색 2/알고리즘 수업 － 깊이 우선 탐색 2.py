import sys

N, M, R = map(int, sys.stdin.readline().split())

graph=[[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

visited=[False]*(N+1)
stack=[R]
visit=[0]*(N+1)

for i in graph:
    i.sort()
i=1
while stack:
    v=stack.pop()
    if not visited[v]:
        visited[v]=True
        visit[v]=i
        i+=1
        stack.extend(graph[v])
        
for i in range(1, N+1):
    print(visit[i])