from collections import deque
import sys
input=lambda:sys.stdin.readline().rstrip()

N = int(input())
arr=[]
for _ in range(N):
    arr.append([0]+list(map(int, input().split()))+[0])
    
for i in range(1, N):
    for j in range(1, len(arr[i])-1):
        arr[i][j]=max(arr[i-1][j-1], arr[i-1][j])+arr[i][j]
print(max(arr[N-1]))