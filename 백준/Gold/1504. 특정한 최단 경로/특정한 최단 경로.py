import sys
from heapq import heappush, heappop
input=lambda:sys.stdin.readline().rstrip()

def find_path(start, destination, graph, N):
    visited=[False for _ in range(N+1)]
    distance = [sys.maxsize for _ in range(N+1)]
    heap=[(0, start)]
    while heap:
        length, node = heappop(heap)
        visited[node] = True
        if node == destination:
            break
        for next_node, weight in graph[node]:
            if not visited[next_node]:
                if length+weight<distance[next_node]:
                    distance[next_node] = length+weight
                    heappush(heap, (length+weight, next_node))
    return distance[destination]

def solve(N, graph, v1, v2):
    start_to_end = find_path(1, N, graph, N)
    start_to_v1 = find_path(1, v1, graph, N)
    v1_to_v2 = find_path(v1, v2, graph, N)
    v2_to_end = find_path(v2, N, graph, N)
    start_to_v2 = find_path(1, v2, graph, N)
    v1_to_end = find_path(v1, N, graph, N)

    if v1 == 1 and v2 == N:
        answer = start_to_end
    elif v1 == 1:
        answer = start_to_v2 + v2_to_end
    elif v2 == N:
        answer = start_to_v1 + v1_to_end
    else:
        answer = min(start_to_v1+v1_to_v2+v2_to_end, start_to_v2+v1_to_v2+v1_to_end)

    if answer >= sys.maxsize:
        return -1
    else:
        return answer

if __name__=="__main__":
    N, E = map(int, input().split())
    graph=dict()
    for i in range(1,N+1):
        graph[i]=[]
    for _ in range(E):
        a, b, weight = map(int, input().split())
        graph[a].append((b, weight))
        graph[b].append((a, weight))
    v1, v2 = map(int, input().split())

    print(solve(N, graph, v1, v2))