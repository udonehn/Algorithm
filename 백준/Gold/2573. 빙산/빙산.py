from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def check(visited, arr, N, M,i,j):
    queue=deque([(i,j)])
    while queue:
        y,x=queue.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx<0 or nx>=M or ny<0 or ny>=N:
                continue
            if visited[ny][nx]==1:
                continue
            if arr[ny][nx]==0:
                continue
            queue.append((ny,nx))
            visited[ny][nx]=1

def melt(arr,N,M):
    m=[]
    for i in range(N):
        for j in range(M):
            if arr[i][j]!=0:
                cnt=0
                for k in range(4):
                    nx,ny=j+dx[k],i+dy[k]
                    if nx<0 or nx>=M or ny<0 or ny>=N:
                        continue
                    if arr[ny][nx]==0:
                        cnt+=1
                m.append([i,j,cnt])
    while m:
        y,x,count=m.pop()
        arr[y][x]-=count
        if arr[y][x]<0:
            arr[y][x]=0

N, M = map(int,input().split())
arr=[]
for _ in range(N):
    arr.append(list(map(int,input().split())))
year=0
while True:
    visited=[[0 for _ in range(M)] for _ in range(N)]
    count=0
    for i in range(N):
        for j in range(M):
            if arr[i][j]!=0 and visited[i][j]==0:
                check(visited,arr,N,M,i,j)
                count+=1
    if count>1:
        break
    if count==0:
        year=0
        break
    melt(arr,N,M)
    year+=1
print(year)