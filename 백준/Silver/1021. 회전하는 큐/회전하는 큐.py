from collections import deque
N, M = map(int, input().split())
deq=deque([i+1 for i in range(N)])
arr=list(map(int, input().split()))
i=0
for target in arr:
    while True:
        if deq[0]==target:
            deq.popleft()
            break
        index = deq.index(target)
        if index<len(deq)/2:
            deq.rotate(-1)
            i+=1
        else:
            deq.rotate(1)
            i+=1
print(i)