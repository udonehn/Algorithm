import sys
from heapq import heappush, heappop
input = lambda:sys.stdin.readline().rstrip()

def solve(graph, start, end, city):
    distance=[sys.maxsize for _ in range(city+1)]
    visited=[False for _ in range(city+1)]

    heap=[]
    heappush(heap, (0, start))

    while heap:
        current_distance, edge = heappop(heap)
        if visited[edge]:
            continue
        visited[edge]=True

        for next, weight in graph[edge]:
            if distance[next]>current_distance+weight:
                distance[next]=current_distance+weight
                heappush(heap, (distance[next], next))

    print(distance[end])

if __name__=="__main__":
    N=int(input())
    M=int(input())
    graph={}
    for i in range(N+1):
        graph[i]=[]
    for _ in range(M):
        start, end, weight = map(int, input().split())
        graph[start].append((end, weight))

    start_city, end_city = map(int, input().split())
    solve(graph, start_city, end_city, N)