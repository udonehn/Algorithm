import sys
input=lambda:sys.stdin.readline().rstrip()

N, M = map(int, input().split())

arr=[]
for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N-1):
        arr[i][j+1]=arr[i][j]+arr[i][j+1]

for _ in range(M):
    x1,y1,x2,y2=map(int,input().split())
    sum=0
    for i in range(x1-1,x2):
        if y1-2>=0:
            sum=sum+arr[i][y2-1]-arr[i][y1-2]
        else:
            sum=sum+arr[i][y2-1]
    print(sum)