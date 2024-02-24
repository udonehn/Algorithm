import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()


def dijkstra(graph, start, X, N):
    distance = [sys.maxsize for _ in range(N+1)]
    distance[start] = 0
    heap = [(0, start)]
    while heap:
        cost, node = heappop(heap)
        if cost > distance[node]:
            continue
        for next_node, next_cost in graph[node]:
            if cost+next_cost > distance[next_node]:
                continue
            distance[next_node] = cost+next_cost
            heappush(heap, (cost+next_cost, next_node))
    return distance[X]


if __name__ == "__main__":
    N, M, X = map(int, input().split())
    graph = dict()
    for i in range(1, N+1):
        graph[i] = []

    for _ in range(M):
        start, end, cost = map(int, input().split())
        graph[start].append((end, cost))

    distance_home_to_party = [-1]
    for i in range(1, N+1):
        distance = dijkstra(graph, i, X, N)
        distance_home_to_party.append(distance)

    distance_party_to_home = [-1]
    for i in range(1, N+1):
        distance = dijkstra(graph, X, i, N)
        distance_party_to_home.append(distance)

    longest_time = 0
    for i in range(1, N+1):
        time = distance_home_to_party[i]+distance_party_to_home[i]
        longest_time = max(longest_time, time)

    print(longest_time)
    