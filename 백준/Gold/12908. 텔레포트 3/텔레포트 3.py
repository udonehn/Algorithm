import sys
input = lambda :sys.stdin.readline()
from heapq import heappush, heappop

def solve(graph):
    queue=[(0,0)]
    distances = [sys.maxsize for _ in range(8)]
    while queue:
        current_distance, current_node = heappop(queue)
        if distances[current_node]<current_distance:
            continue
        for next_node, next_distance in graph[current_node]:
            if distances[next_node]<current_distance+next_distance:
                continue
            distances[next_node] = current_distance+next_distance
            heappush(queue, (current_distance+next_distance,next_node))

    return distances[1]


if __name__=="__main__":
    s = tuple(map(int, input().split()))
    e = tuple(map(int, input().split()))
    node = [s,e]
    count=0
    for _ in range(3):
        x1, y1, x2, y2 = tuple(map(int, input().split()))
        node.append((x1, y1))
        node.append((x2, y2))

    graph=dict()
    for i in range(8):
        graph[i]=[]

    for i in range(8):
        x1, y1 = node[i]
        for j in range(i+1,8):
            x2, y2 = node[j]
            if i>1 and i%2==0 and j-i==1:
                graph[i].append((j,10))
                graph[j].append((i,10))
            else:
                graph[i].append((j, abs(x1 - x2) + abs(y1 - y2)))
                graph[j].append((i, abs(x1 - x2) + abs(y1 - y2)))

    print(solve(graph))