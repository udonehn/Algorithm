M, N = map(int, input().split())

arr = [[0 for j in range(N)] for i in range(M)]
for i in range(M):
    lst = list(input())
    for j in range(N):
        arr[i][j] = lst[j]
min = N*N
i=0
while True:
    j=0
    while True:
        for wb in range(2):
            if wb == 0:
                start = 'W'
            else:
                start = 'B'
            cnt=0
            k=0
            while k<8:
                l=0
                while l<8:
                    if start!=arr[k+i][l+j]:
                        cnt+=1
                    if start == 'W':
                        start ='B'
                    else:
                        start = 'W'
                    l+=1
                k+=1
                if start == 'W':
                    start ='B'
                else:
                    start = 'W'
            if cnt < min:
                min = cnt
        j+=1
        if j>N-8:
            break
    i+=1
    if i>M-8:
        break
print(min)