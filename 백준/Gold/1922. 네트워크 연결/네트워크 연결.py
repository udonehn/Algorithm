from heapq import heappop, heappush
import sys
input = lambda:sys.stdin.readline().rstrip()


def solve(N, graph):
    heap = [(0, 1)]
    visited = [False for _ in range(N+1)]
    result = 0

    while heap:
        cost, node = heappop(heap)
        if visited[node]:
            continue
        visited[node] = True
        result+=cost

        for next_node, next_cost in graph[node]:
            if visited[next_node]:
                continue
            heappush(heap, (next_cost, next_node))

    return result


if __name__ == "__main__":
    N = int(input())
    M = int(input())

    graph=dict()
    for i in range(1, N+1):
        graph[i]=[]

    for _ in range(M):
        A, B, cost = map(int, input().split())
        graph[A].append((B, cost))
        graph[B].append((A, cost))

    print(solve(N, graph))