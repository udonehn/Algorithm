import sys
from collections import deque
input=lambda:sys.stdin.readline().rstrip()

def check(arr,l,r):
    if l>r:
        return 0
    if arr[l]<arr[r]:   #왼쪽이 빠른 경우
        return 0
    elif arr[l]>arr[r]: #오른쪽이 빠른 경우
        return 1
    else:
        return check(arr,l+1,r-1)

N=int(input())
arr=deque()
for _ in range(N):
    arr.append(input())

ans=[]
l,r=0,N-1
while arr:
    if check(arr,0,len(arr)-1)==0:
        ans.append(arr.popleft())
    else:
        ans.append(arr.pop())

for i in range(1,N+1):
    print(ans[i-1],end='')
    if i%80==0:
        print()