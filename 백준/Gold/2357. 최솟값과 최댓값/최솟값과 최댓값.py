import sys
input=lambda:sys.stdin.readline().rstrip()

# 트리 생성
N, M = map(int, input().split())
arr=[]
for _ in range(N):
    arr.append(int(input()))
arr_max = max(arr)
arr_min = min(arr)

k=1
while 2**k < N:
    k+=1

min_tree = [arr_max] * 2**(k+1)
max_tree = [arr_min] * 2**(k+1)

for i in range(N):
    min_tree[2**k+i]=arr[i]
    max_tree[2**k+i]=arr[i]

for i in range(2**k-1,0,-1):
    min_tree[i] = min(min_tree[i*2],min_tree[i*2+1])
    max_tree[i] = max(max_tree[i*2],max_tree[i*2+1])

# 쿼리 시작
for _ in range(M):
    a, b = map(int, input().split())

    ans_min=arr_max
    ans_max=arr_min
    start,end = a+2**k-1, b+2**k-1

    while start<=end:
        if start%2==1:
            ans_min=min(ans_min, min_tree[start])
            ans_max=max(ans_max, max_tree[start])
        start = (start+1)//2
        
        if end%2==0:
            ans_min=min(ans_min, min_tree[end])
            ans_max=max(ans_max, max_tree[end])
        end = (end-1)//2

    print(ans_min, ans_max)