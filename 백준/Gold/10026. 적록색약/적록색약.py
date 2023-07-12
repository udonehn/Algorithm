import sys
input=lambda: sys.stdin.readline().rstrip()

xs=[1,-1,0,0]
ys=[0,0,1,-1]

def DFS(graph,i,j):
    c=graph[i][j]
    stack=[(i,j)]
    while stack:
        x,y=stack.pop()
        graph[x][y]=0
        for i in range(4):
            xx=x+xs[i]
            yy=y+ys[i]
            if xx<0 or xx>=len(graph) or yy<0 or yy>=len(graph):
                continue
            if graph[xx][yy]==c:
                stack.append((xx,yy))
                
N=int(input())

graph=[]
for _ in range(N):
    graph.append(list(input()))
    
graph2=[[] for _ in range(N)]
for i in range(N):
    graph2[i].extend(graph[i])

count=0
for i in range(N):
    for j in range(N):
        if graph[i][j]!=0:
            DFS(graph, i, j)
            count+=1

for i in range(N):
    for j in range(N):
        if graph2[i][j]=='R':
            graph2[i][j]='G'

count2=0
for i in range(N):
    for j in range(N):
        if graph2[i][j]!=0:
            DFS(graph2, i, j)
            count2+=1
            
print(count, count2)