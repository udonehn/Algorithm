import sys
from collections import deque
input=lambda:sys.stdin.readline().rstrip()
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def inout(arr,col,row):
    arr[0][0]-=1
    queue=deque([(0,0)])
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx<0 or nx>=row or ny<0 or ny>=col:
                continue
            if (arr[ny][nx]!=arr[0][0]) and (arr[ny][nx]!=1):
                queue.append((nx,ny))
                arr[ny][nx]=arr[0][0]

def check(arr,col,row):
    c=[]
    for i in range(col):
        for j in range(row):
            if arr[i][j]==1:
                cnt=0
                for k in range(4):
                    x,y=j+dx[k],i+dy[k]
                    if x<0 or x>=row or y<0 or y>=col:
                        continue
                    if arr[y][x]<=-1:
                        cnt+=1
                if cnt>0:
                    c.append((j,i))
    return c

def count(arr):
    cnt=0
    for i in arr:
        for j in i:
            if j==1:
                cnt+=1
    return cnt

col,row=map(int, input().split())
arr=[list(map(int, input().split())) for _ in range(col)]

time=0
cnt=0
while True:
    inout(arr,col,row)
    c=check(arr,col,row)
    if len(c)==0:
        break
    cnt=count(arr)
    for x,y in c:
        arr[y][x]=arr[0][0]
    time+=1

print(time)
print(cnt)