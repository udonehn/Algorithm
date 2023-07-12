import sys
input=lambda:sys.stdin.readline().rstrip()
dx=[0,0,-1,1]
dy=[-1,1,0,0]

R, C = map(int, input().split())

arr=[]
for _ in range(R):
    arr.append(list(input()))
    
alpha=[False]*26 #A=65
stack=[(0,0,alpha)]
m=0
while stack:
    x,y,alpha=stack.pop()
    alpha=alpha[:]
    alpha[ord(arr[y][x])-65]=True
    count=0
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if nx<0 or nx>=C or ny<0 or ny>=R:
            continue
        if alpha[ord(arr[ny][nx])-65]==False:
            stack.append((nx,ny,alpha))
            count+=1
    if count==0:
        c=0
        for i in alpha:
            if i==True:
                c+=1
        m=max(m,c)
print(m)