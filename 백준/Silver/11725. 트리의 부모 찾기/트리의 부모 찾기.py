import sys
from collections import deque
input=lambda:sys.stdin.readline().rstrip()

def DFS(graph,N):
    parents=[i for i in range(N+1)]
    stack=[1]
    visited=set()
    
    while stack:
        p=stack.pop()
        for i in graph[p]:
            if i not in visited:
                parents[i]=p
                stack.append(i)
                visited.add(i)
    return parents
    

N=int(input())

graph={}

for i in range(1,N+1):
    graph[i]=[]

for _ in range(N-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

parents = DFS(graph,N)

for i in parents[2:]:
    print(i)