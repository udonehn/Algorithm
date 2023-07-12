from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def BFS(arr,N,M):
    queue=deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j]==2:
                queue.append((j,i))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx<0 or nx>=M or ny<0 or ny>=N:
                continue
            if arr[ny][nx]==1:
                continue
            if arr[ny][nx]==0:
                queue.append((nx,ny))
                arr[ny][nx]=2
    count=0 
    for i in range(N):
        for j in range(M):
            if arr[i][j]==0:
                count+=1
    return count
                
arr=[]
N, M = map(int, input().split())
for _ in range(N):
    arr.append(list(map(int, input().split())))
    
zero=[]
for i in range(N):
    for j in range(M):
        if arr[i][j]==0:
            zero.append([j,i])

max=0
for i in range(len(zero)):
    for j in range(i+1,len(zero)):
        for k in range(j+1,len(zero)):
            a=[]
            for l in range(N):
                a.append([m for m in arr[l]])
            x,y=zero[i]
            a[y][x]=1
            x,y=zero[j]
            a[y][x]=1
            x,y=zero[k]
            a[y][x]=1
            
            m=BFS(a, N, M)
            if m>max:
                max=m
print(max)