import sys
from collections import deque
input=lambda:sys.stdin.readline().rstrip()

def check(a,i):
    num=str(i)
    ans=str(a[0])
    strike,ball=0,0
    for j in range(3):
        for k in range(3):
            if num[j]==ans[k]:
                if j==k:
                    strike+=1
                else:
                    ball+=1
    if strike==a[1] and ball==a[2]:
        return True
    else:
        return False
        

N=int(input())
arr=[]
for _ in range(N):
    arr.append(list(map(int,input().split())))
    
count=0
for i in range(101, 1000):
    i=str(i)
    TF=False
    
    for j in list(i):
        if j=='0':
            TF=True
            
    for j in range(3):
        for k in range(3):
            if i[j]==i[k] and j!=k:
                TF=True
    
    if TF:
        continue
    
    cnt=0
    for a in arr:
        if check(a,i)==True:
            cnt+=1
    if cnt==N:
        count+=1
print(count)