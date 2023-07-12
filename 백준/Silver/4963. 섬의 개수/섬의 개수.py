import sys
from collections import deque
input=lambda:sys.stdin.readline().rstrip()

dx=[-1,-1,-1,0,0,1,1,1]
dy=[1,0,-1,1,-1,1,0,-1]

def check(arr,x,y,w,h):
    queue=deque()
    queue.append((x,y))
    arr[y][x]='0'
    while queue:
        x,y=queue.popleft()
        for i in range(8):
            nx,ny=x+dx[i],y+dy[i]
            if nx<0 or nx>=w or ny<0 or ny>=h:
                continue
            if arr[ny][nx]=='1':
                queue.append((nx,ny))
                arr[ny][nx]='0'

while True:
    w, h = map(int,input().split())
    if w==0 and h==0:
        break
    
    arr=[]
    for _ in range(h):
        arr.append(input().split())
    
    count=0
    for i in range(h):
        for j in range(w):
            if arr[i][j]=='1':
                check(arr,j,i,w,h)
                count+=1
                
    print(count)