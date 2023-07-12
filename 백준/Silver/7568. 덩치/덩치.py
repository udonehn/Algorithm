arr=[]
N=int(input())
for _ in range(N):
    arr.append(list(map(int, input().split())))
rank=[]
for i in range(N):
    count=0
    for j in range(N):
        if arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]:
            count+=1
    rank.append(count)
for i in rank:
    print(i+1,end=' ')