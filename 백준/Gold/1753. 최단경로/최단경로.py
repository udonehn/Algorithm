import sys
input = lambda:sys.stdin.readline().rstrip()

def solve(graph, V, E, K):
    INF=11*E
    distance=[INF for _ in range(V+1)]
    visited=[False for _ in range(V+1)]
    distance[K]=0

    while True:
        vertex=0
        vertex_distance=INF
        for i in range(1,V+1):
            if visited[i]:
                continue
            if distance[i]<=vertex_distance:
                vertex=i
                vertex_distance=distance[i]
        if vertex==0:
            break

        for v, w in graph[vertex]:
            if distance[vertex]+w<distance[v]:
                distance[v]=distance[vertex]+w

        visited[vertex]=True

    for i in range(1,V+1):
        if distance[i]==INF:
            print("INF")
        else:
            print(distance[i])



if __name__=="__main__":
    V, E = map(int, input().split())
    K=int(input())
    graph={}
    for i in range(V):
        graph[i+1]=[]
    for _ in range(E):
        u,v,w=map(int, input().split())
        graph[u].append((v,w))

    solve(graph, V, E, K)