N = int(input())
M = int(input())

graph=[[]for _ in range(N+1)]
for _ in range(M):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited=[False]*(N+1)
stack=[1]
count=0
while stack:
    v=stack.pop()
    if not visited[v]:
        visited[v]=True
        count+=1
        stack.extend(graph[v])
print(count-1)