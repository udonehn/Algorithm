from collections import deque

dx=[-2,-1,1,2,2,1,-1,-2]
dy=[1,2,2,1,-1,-2,-2,-1]

def BFS(arr,x,y):
    queue=deque([(x,y)])
    while queue:
        x,y=queue.popleft()
        for i in range(8):
            nx,ny=x+dx[i],y+dy[i]
            if nx<0 or nx>=len(arr) or ny<0 or ny>=len(arr):
                continue
            if arr[ny][nx]==0:
                arr[ny][nx]=arr[y][x]+1
                queue.append((nx,ny))
            
for _ in range(int(input())):
    I=int(input())
    arr=[[0 for _ in range(I)] for _ in range(I)]
    x,y=map(int,input().split())
    arr[y][x]=1
    BFS(arr,x,y)
    x,y=map(int,input().split())
    print(arr[y][x]-1)