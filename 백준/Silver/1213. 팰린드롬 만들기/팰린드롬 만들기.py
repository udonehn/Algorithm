from collections import deque
import sys
input=lambda:sys.stdin.readline().rstrip()

s=list(input())

a=dict()
for i in s:
    if i in a:
        a[i]+=1
    else:
        a[i]=1

cnt=0
for i in a.keys():
    if a[i]%2==1:
        cnt+=1
        r=i

if cnt>1:
    print("I'm Sorry Hansoo")
else:
    if cnt==0:
        p=deque()
    elif cnt==1:
        p=deque([r])
        a[r]-=1
    
    k=sorted(list(a.keys()),reverse=True)
    for i in k:
        while a[i]!=0:
            a[i]-=2
            p.append(i)
            p.appendleft(i)

    print(''.join(list(p)))