import sys
input=lambda:sys.stdin.readline().rstrip()

N=int(input())
arr=[0]
arr.extend(list(map(int,input().split())))

M=int(input())
ij=[]
for _ in range(M):
    ij.append(list(map(int,input().split())))

for i in range(N):
    arr[i+1]+=arr[i]

for i in ij:
    print(arr[i[1]]-arr[i[0]-1])