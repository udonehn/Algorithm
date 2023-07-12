from collections import deque
from heapq import heappop, heappush
import sys
input=lambda:sys.stdin.readline().rstrip()

N=int(input())
heap=[]

for _ in range(N):
    p,d=map(int,input().split())
    heappush(heap,(-p,d))

v=set()
sum=0
while heap:
    p,d=heappop(heap)
    i=d
    while True:
        if i not in v:
            break
        else:
            i-=1
    if i>0:
        v.add(i)
        sum+=-p
    
print(sum)