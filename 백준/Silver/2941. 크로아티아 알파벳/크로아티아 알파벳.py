from collections import deque
alpha=['c=','c-','dz=','d-','lj','nj','s=','z=']

ipt=deque(input())
cnt=0
while ipt:
    if len(ipt)>=3 and ipt[0]+ipt[1]+ipt[2] in alpha:
        p=3
    elif len(ipt)>=2 and ipt[0]+ipt[1] in alpha:
        p=2
    else:
        p=1
    for _ in range(p):
        ipt.popleft()
    cnt+=1
print(cnt)