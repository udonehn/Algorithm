from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def BFS(arr,M,N):
    queue=deque()
    s=0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                queue.append((j,i))
                s+=1
                
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx<0 or nx>=M or ny<0 or ny>=N:
                continue
            if arr[ny][nx]==-1:
                continue
            if arr[ny][nx]==0:
                arr[ny][nx]=arr[y][x]+1
                queue.append((nx,ny))
        
M,N=map(int, input().split())
arr=[]
for _ in range(N):
    arr.append(list(map(int,input().split())))
BFS(arr,M,N)
a=[]
TF=True
for i in arr:
    a.append(max(i))
    if 0 in i:
        TF=False
if TF==True:
    print(max(a)-1)
else:
    print(-1)