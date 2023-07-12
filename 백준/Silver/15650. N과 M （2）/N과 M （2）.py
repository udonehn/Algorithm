import sys
import itertools
input=lambda:sys.stdin.readline().rstrip()

def check(i):
    c=i[0]
    for j in i:
        if j<c:
            return False
        c=j
    return True

N,M=map(int,input().split())
for i in list(itertools.permutations(list(range(1,N+1)),M)):
    if check(i):
        for j in i:
            print(j, end=' ')
        print()