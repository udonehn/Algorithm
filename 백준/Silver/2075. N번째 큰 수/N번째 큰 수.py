import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

N=int(input())
heap=[]

for i in list(map(int,input().split())):
    heapq.heappush(heap, i)

for _ in range(N-1):
    for i in list(map(int,input().split())):
        heapq.heappush(heap, i)
        
    for _ in range(N):
        heapq.heappop(heap)

print(heapq.heappop(heap))