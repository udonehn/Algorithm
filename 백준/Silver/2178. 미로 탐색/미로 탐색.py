from collections import deque
import sys

dx=[0,0,-1,1]
dy=[1,-1,0,0]

def BFS(arr,N,M):
    queue=deque([(0,0)])
    arr[0][0]=1
    while queue:
        y,x=queue.popleft()
        for i in range(4):
            ny,nx=y+dy[i],x+dx[i]
            if nx<0 or nx>=M or ny<0 or ny>=N:
                continue
            if arr[ny][nx]==1 and arr[ny][nx]!=0:
                arr[ny][nx]=arr[y][x]+1
                queue.append((ny,nx))
    return arr[N-1][M-1]

N, M = map(int, sys.stdin.readline().rstrip().split())
arr=[]
for _ in range(N):
    arr.append(list(map(int, list(sys.stdin.readline().rstrip()))))
print(BFS(arr,N,M))