from collections import deque
N = int(input())
deq=deque()
for _ in range(N):
    a, b = map(int, input().split())
    arr=input().split()
    for i in arr:
        deq.append(i)
    i=0
    index=b
    while True:
        if deq[0]==max(deq):
            aa = deq.popleft()
            i+=1
            index-=1
            if index == -1:
                break
        else:
            x = deq.popleft()
            deq.append(x)
            index-=1
            if index==-1:
                index=len(deq)-1
    print(i)
    deq.clear()