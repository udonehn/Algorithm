A, B = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(len(arr)):
    if(arr[i]<B):
        print(arr[i], end=' ')