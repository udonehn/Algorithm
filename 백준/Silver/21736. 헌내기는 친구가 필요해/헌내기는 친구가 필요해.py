import sys
from collections import deque
input=lambda:sys.stdin.readline().rstrip()
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def findI(arr,N,M):
    for i in range(N):
        for j in range(M):
            if arr[i][j]=='I':
                return j,i

N, M = map(int,input().split())
arr=[]
for _ in range(N):
    arr.append(list(input()))
x,y=findI(arr,N,M)

queue=deque([(x,y)])

count=0
while queue:
    x,y=queue.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if nx<0 or nx>=M or ny<0 or ny>=N:
            continue
        if arr[ny][nx]=='X':
            continue
        if arr[ny][nx]=='P':
            count+=1
        arr[ny][nx]='X'
        queue.append((nx,ny))

if count==0:
    print('TT')
else:
    print(count)