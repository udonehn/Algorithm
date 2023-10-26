import sys
from heapq import heappush, heappop
input=lambda:sys.stdin.readline().rstrip()

def solve(node, edge, graph, departure, arrival):
    visited=[False for _ in range(node+1)]
    path_length=[sys.maxsize for _ in range(node+1)]
    answer_route=[[] for _ in range(node+1)]
    path_length[departure]=0
    heap=[(0, departure, [departure])]

    while heap:
        path, node, route = heappop(heap)
        visited[node]=True
        if path>path_length[node]:
            continue

        for new_node, new_path in graph[node]:
            if not visited[new_node]:
                if path+new_path<path_length[new_node]:
                    path_length[new_node]=path+new_path
                    heappush(heap, (path+new_path, new_node, route+[new_node]))
                    answer_route[new_node]=route+[new_node]

    print(path_length[arrival])
    print(len(answer_route[arrival]))
    print(' '.join(list(map(str, answer_route[arrival]))))


if __name__=="__main__":
    n=int(input())
    graph={}
    for i in range(1,n+1):
        graph[i]=[]
    m=int(input())

    for _ in range(m):
        start, end, weight = map(int, input().split())
        graph[start].append((end,weight))

    departure, arrival = map(int, input().split())

    solve(n, m, graph, departure, arrival)