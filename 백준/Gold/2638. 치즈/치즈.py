from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def check(arr, N, M):
    for i in range(N):
        for j in range(M):
            if arr[i][j]==1:
                return True
    return False

def inout(arr,N,M):
    queue=deque([(0,0)])
    arr[0][0]-=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx<0 or nx>=M or ny<0 or ny>=N:
                continue
            if arr[ny][nx]==1:
                continue
            if arr[ny][nx]!=arr[0][0]:
                queue.append((nx,ny))
                arr[ny][nx]=arr[0][0]

def melt(arr, N, M):
    m=[]
    for i in range(N):
        for j in range(M):
            if arr[i][j]==1:
                count=0
                for k in range(4):
                    nx,ny=+j+dx[k],i+dy[k]
                    if nx<0 or nx>=M or ny<0 or ny>=N:
                        continue
                    if arr[ny][nx]<0:
                        count+=1
                if count>=2:
                    m.append([j,i])
    return m

N, M=map(int, input().split())
arr=[]
for _ in range(N):
    arr.append(list(map(int,input().split())))

cnt=0
while(check(arr, N, M)):
    inout(arr,N,M)
    m=melt(arr,N,M)
    for i in m:
        arr[i[1]][i[0]]=-1
    cnt+=1
    
print(cnt)