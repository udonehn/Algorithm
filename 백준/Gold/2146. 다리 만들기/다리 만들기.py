import sys
from collections import deque
input=lambda:sys.stdin.readline().rstrip()
dx=[0,0,1,-1]
dy=[1,-1,0,0]


def BFS(arr,x,y,isl,N):
    country=[]
    for i in arr:
        country.append([j for j in i])
    
    queue=deque([(x,y)])
    country[y][x]=1
    b=N*N
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            if country[ny][nx]>0:
                continue
            if country[ny][nx]<0:
                if arr[ny][nx]!=isl:
                    b = min(b,country[y][x])
            if country[ny][nx]==0:
                country[ny][nx]=country[y][x]+1
                queue.append((nx,ny))
    return b

def solve(N,arr):
    island=-1
    for i in range(N):
        for j in range(N):
            if arr[i][j]==1:
                queue=deque([(j,i)])
                arr[i][j]=island
                while queue:
                    x,y=queue.popleft()
                    for k in range(4):
                        nx,ny=x+dx[k],y+dy[k]
                        if nx<0 or nx>=N or ny<0 or ny>=N:
                            continue
                        if arr[ny][nx]==1:
                            arr[ny][nx]=island
                            queue.append((nx,ny))
                island-=1

    beach=[]
    for i in range(N):
        for j in range(N):
            if arr[i][j]==0:
                isl=0
                cnt=set()
                for k in range(4):
                    nx,ny=j+dx[k],i+dy[k]
                    if nx<0 or nx>=N or ny<0 or ny>=N:
                        continue
                    if arr[ny][nx]<0:
                        cnt.add(arr[ny][nx])
                if len(cnt)>1:
                    return 1
                if len(cnt)==1:
                    isl = list(cnt)[0]
                if isl<0:
                    beach.append((j,i,isl))
    
    bridge=N*N
    for x,y,isl in beach:
        bridge=min(bridge, BFS(arr,x,y,isl,N))

    return bridge

N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
print(solve(N, arr))