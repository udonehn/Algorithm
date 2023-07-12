from collections import deque

N = int(input())
deq = deque()
ans=[]
for _ in range(N):
    c = input().split()
    if c[0]=='push':
        deq.append(c[1])
    elif c[0] == 'pop':
        if len(deq)==0:
            ans.append(-1)
        else:
            ans.append(deq.popleft())
    elif c[0] == 'size':
        ans.append(len(deq))
    elif c[0] == 'empty':
        if len(deq)==0:
            ans.append(1)
        else:
            ans.append(0)
    elif c[0] == 'front':
        if len(deq) == 0:
            ans.append(-1)
        else:
            ans.append(deq[0])
    elif c[0] == 'back':
        if len(deq) == 0:
            ans.append(-1)
        else:
            ans.append(deq[-1])
for i in ans:
    print(i)