from heapq import heappop, heappush
import sys
input=lambda:sys.stdin.readline().rstrip()

N=int(input())
heap=[]

for _ in range(N):
    x = int(input())
    if x==0:
        if len(heap)==0:
            print(0)
        else:
            print(-heappop(heap))
    else:
        heappush(heap,-x)