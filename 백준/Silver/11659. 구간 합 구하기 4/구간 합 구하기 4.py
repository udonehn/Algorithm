import sys
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

ps=[]
ps.append(arr[0])
for i in range(1, len(arr)):
    ps.append(ps[i-1]+arr[i])

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    if i-2>=0:
        print(ps[j-1]-ps[i-2])
    else:
        print(ps[j-1])