import sys
from heapq import heappop, heappush
input=lambda:sys.stdin.readline().rstrip()

N=int(input())
heap=[]

for _ in range(N):
    heappush(heap,(int(input())))

sum=0
while len(heap)>1:
    A=heappop(heap)
    B=heappop(heap)
    sum+=A+B
    heappush(heap, A+B)
    
print(sum)