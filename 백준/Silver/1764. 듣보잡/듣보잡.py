import sys
N, M = map(int, sys.stdin.readline().split())
d = set()
b = set()
for i in range(N):
    d.add(sys.stdin.readline())
for i in range(M):
    b.add(sys.stdin.readline())
db = sorted(list(d&b))
print(len(db))
for i in db:
    print(i,end='')