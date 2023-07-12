from collections import deque
import sys
input=lambda:sys.stdin.readline().rstrip()

def ro(n):
    i=int(n)
    if n-i<0.5:
        return i
    else:
        return i+1

n=int(input())

arr=[]
for _ in range(n):
    arr.append(int(input()))

arr=deque(sorted(arr))
j=ro(n*0.15)
for _ in range(j):
    arr.pop()
    arr.popleft()
if len(arr)==0:
    print(0)
else:
    print(ro(sum(arr)/len(arr)))