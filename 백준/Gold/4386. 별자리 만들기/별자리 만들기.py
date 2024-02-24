import sys
import math
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()


def solve(N, arr):
    graph = dict()
    for i in range(N):
        graph[i] = []
    for i in range(N):
        for j in range(i+1, N):
            distance = math.sqrt((arr[i][0] - arr[j][0])**2 + (arr[i][1] - arr[j][1])**2)
            graph[i].append((j, distance))
            graph[j].append((i, distance))
    visited = [False for _ in range(N)]
    heap = [(0, 0)]
    answer = 0
    while heap:
        cost, node = heappop(heap)
        if visited[node]:
            continue
        visited[node] = True
        answer += cost
        for next_node, next_cost in graph[node]:
            heappush(heap, (next_cost, next_node))
    return round(answer, 2)


if __name__ == "__main__":
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(float, input().split())))
    print(solve(N, arr))
