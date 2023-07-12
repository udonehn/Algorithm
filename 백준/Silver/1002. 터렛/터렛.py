import sys
import math
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    d=math.sqrt(abs(x1-x2)**2+abs(y1-y2)**2)
    if d==0: #좌표가 같을 때
        if r1==r2:
            ans=-1
        else:
            ans=0
    elif d<max(r1,r2): #원이 원 안에 있을 때
        if d+min(r1,r2)>max(r1,r2):
            ans=2
        elif d+min(r1,r2)==max(r1,r2):
            ans=1
        else:
            ans=0
    else:   #원이 원 안에 있지 않을 때
        if r1+r2>d:
            ans=2
        elif r1+r2==d:
            ans=1
        else:
            ans=0
    print(ans)