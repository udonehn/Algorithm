import sys
from heapq import heappop, heappush, heapify
input=lambda:sys.stdin.readline().rstrip()

for _ in range(int(input())):
    K=int(input())
    heap=list(map(int, input().split()))
    heapify(heap)
    ans=0
    while len(heap)>1:
        tmp1=heappop(heap)
        tmp2=heappop(heap)
        ans+=tmp1+tmp2
        heappush(heap, tmp1+tmp2)
    print(ans)