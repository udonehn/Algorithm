M, N = map(int, input().split())

arr = []
for i in range(0, N+1):
    arr.append(True)

arr[0] = False
arr[1] = False
index = 2

while index<=N:
    while arr[index]!=True and index != N:
        index+=1
    i = 2
    ii=index*i
    while ii <= N:
        arr[ii]=False
        i+=1
        ii=index*i
    index+=1
    
for i in range(M, N+1):
    if arr[i]:
        print(i)