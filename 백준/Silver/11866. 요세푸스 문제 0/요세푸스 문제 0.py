from collections import deque

N,K=map(int,input().split())
queue=deque(range(1,N+1))
arr=[]
while queue:
    for _ in range(K-1):
        queue.append(queue.popleft())
    arr.append(str(queue.popleft()))
print('<',end='')
print(', '.join(arr),end='')
print('>',end='')