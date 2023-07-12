import sys
from collections import deque
input=lambda:sys.stdin.readline().rstrip()
dx=[0,0,1,-1,0,0]
dy=[1,-1,0,0,0,0]
dz=[0,0,0,0,1,-1]


def solve(arr,M,N,H):
    queue=deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k]==1:
                    queue.append((i,j,k))
    while queue:
        level,row,column=queue.popleft()
        for i in range(6):
            nl,nr,nc=level+dx[i],row+dy[i],column+dz[i]
            if nl<0 or nl>=H or nr<0 or nr>=N or nc<0 or nc>=M:
                continue
            if arr[nl][nr][nc]!=0:
                continue
            arr[nl][nr][nc]=arr[level][row][column]+1
            queue.append((nl,nr,nc))
    m=0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k]==0:
                    return -1
                else:
                    m=max(m,arr[i][j][k])
    return m-1

M,N,H=map(int, input().split())
arr=[[list(map(int, input().split())) for _ in range(N)]for _ in range(H)]

print(solve(arr,M,N,H))