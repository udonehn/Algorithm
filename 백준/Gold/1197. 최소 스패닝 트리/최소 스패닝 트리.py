import sys
from heapq import heappop, heappush
input = lambda:sys.stdin.readline().rstrip()


def prim_MST(graph, V):
    visited=[False for _ in range(V+1)]
    heap=[(0, 1)]
    answer=0
    while heap:
        cost, vertex = heappop(heap)
        if visited[vertex]:
            continue
        visited[vertex]=True
        answer+=cost
        for new_cost, new_vertex in graph[vertex]:
            heappush(heap, (new_cost, new_vertex))
    return answer


if __name__=="__main__":
    V, E = map(int, input().split())
    graph=dict()
    for i in range(1, V+1):
        graph[i]=[]
    for _ in range(E):
        A, B, cost = map(int,input().split())
        graph[A].append((cost, B))
        graph[B].append((cost, A))
    print(prim_MST(graph, V))