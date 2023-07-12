from collections import deque

xs=[0,0,1,-1]
ys=[1,-1,0,0]

def BFS(graph, x, y):
    count=1
    graph[x][y]=0
    queue=deque([(x,y)])
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            xx,yy=x+xs[i],y+ys[i]
            if xx<0 or xx>=len(graph) or yy<0 or yy>=len(graph):
                continue
            if graph[xx][yy]==1:
                graph[xx][yy]=0
                queue.append((xx,yy))
                count+=1
    return count

N = int(input())

graph=[]
for _ in range(N):
    graph.append(list(map(int, list(input()))))
house=[]

for i in range(N):
    for j in range(N):
        if graph[i][j]==1:
            house.append(BFS(graph, i, j))
            
house.sort()
print(len(house))
for i in house:
    print(i)