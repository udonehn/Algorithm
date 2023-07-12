import sys
from collections import deque
input=lambda:sys.stdin.readline().rstrip()
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def BFS(map,i,j,row,column):
    arr=[]
    for l in map:
        arr.append([ll for ll in l])
    
    queue=deque([(j,i)])
    arr[i][j]=0
    m=0
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx<0 or nx>=column or ny<0 or ny>=row:
                continue
            if arr[ny][nx]=='L':
                arr[ny][nx]=arr[y][x]+1
                m=max(m,arr[y][x]+1)
                queue.append((nx,ny))
    return m


row, column = map(int,input().split())
map=[list(input()) for _ in range(row)]

ans=0
for i in range(row):
    for j in range(column):
        if map[i][j]=='L':
            ans=max(ans,BFS(map,i,j,row,column))

print(ans)