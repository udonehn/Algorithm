from heapq import heappop, heappush
import sys
input=lambda:sys.stdin.readline().rstrip()

N=int(input())
heap=[]

for _ in range(N):
    heappush(heap, tuple(map(int,input().split()[1:])))
    
classroom=[]
heappush(classroom, heappop(heap)[1])

while heap:
    n=heappop(heap)
    if classroom[0]>n[0]:
        heappush(classroom, n[1])
    else:
        heappop(classroom)
        heappush(classroom, n[1])
        
print(len(classroom))