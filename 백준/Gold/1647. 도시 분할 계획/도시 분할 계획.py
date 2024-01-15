import sys
from heapq import heappush, heappop
import random
input = lambda: sys.stdin.readline().rstrip()

def solve(N, M, graph):
    visited=set()
    sum_cost=0
    max_cost=0
    start = random.randrange(1,N+1)
    queue=[(0, start)]

    while queue:
        cost, node = heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        max_cost = max(max_cost, cost)
        sum_cost+=cost
        for new_node, new_cost in graph[node]:
            if new_node not in visited:
                heappush(queue, (new_cost, new_node))

    return sum_cost-max_cost

if __name__=="__main__":
    N, M = map(int, input().split())
    graph=dict()
    for i in range(1, N+1):
        graph[i]=[]
    for _ in range(M):
        A,B,C = map(int, input().split())
        graph[A].append((B,C))
        graph[B].append((A,C))
    print(solve(N, M, graph))