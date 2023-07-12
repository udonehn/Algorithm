from collections import deque
import sys
input=lambda:sys.stdin.readline().rstrip()

N, K = map(int, input().split())
time=dict()
time[N]=0
count=[1 for _ in range(100001)]
queue=deque([(N)])

while queue:
    s=queue.popleft()
    
    for n in (s*2,s+1,s-1):
        if 0<=n<=100000:
            if n not in time:
                time[n]=time[s]+1
                count[n]=1
                queue.append(n)
            elif time[n]==time[s]+1:
                count[n]+=1
                queue.append(n)
                
print(time[K])
print(count[K])