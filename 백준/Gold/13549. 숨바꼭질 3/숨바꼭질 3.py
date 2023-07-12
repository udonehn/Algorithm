from collections import deque
import sys
input=lambda:sys.stdin.readline().rstrip()

N, K = map(int, input().split())
arr=dict()
arr[N]=0
queue=deque([(N)])

while queue:
    s=queue.popleft()
    
    n=s*2
    if 0<=n<=100000 and (n not in arr or arr[n]>arr[s]):
        arr[n]=arr[s]
        queue.append(n)
        
    n=s+1
    if 0<=n<=100000 and (n not in arr or arr[n]>arr[s]+1):
        arr[n]=arr[s]+1
        queue.append(n)
            
    n=s-1
    if 0<=n<=100000 and (n not in arr or arr[n]>arr[s]+1):
        arr[n]=arr[s]+1
        queue.append(n)
        
print(arr[K])