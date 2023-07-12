def binary_search(key, low, high, arr):
    if low>high:
        return -1
    mid = (low+high)//2
    if arr[mid]>key:
        return binary_search(key, low, mid-1, arr)
    elif arr[mid]<key:
        return binary_search(key, mid+1, high, arr)
    elif arr[mid] == key:
        return mid

int(input())
A = []
A= list(map(int, input().split()))
A.sort()
int(input())
B = []
B = list(map(int, input().split()))

for i in B:
    if binary_search(i, 0, len(A)-1, A)>=0:
        print(1)
    else:
        print(0)