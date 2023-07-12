from collections import deque
import sys
input=lambda:sys.stdin.readline().rstrip()

N, K = map(int, input().split())
visited=set()
visited.add(N)
queue=deque([(N,[N])])

if N<=K:
    while True:
        s,path=queue.popleft()
        if s==K:
            break
        
        for n in (s+1,s-1,s*2):
            if 0<=n<=100000 and n not in visited:
                visited.add(n)
                queue.append((n,path+[n]))
                
    print(len(path)-1)
    print(' '.join(map(str,path)))
else:
    print(N-K)
    print(' '.join(map(str,range(N,K-1,-1))))