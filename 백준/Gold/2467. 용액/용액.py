import sys
input = lambda:sys.stdin.readline()

def choose(arr, start, end):
    tmp=[]
    tmp.append(abs(arr[start + 1] + arr[end]))
    tmp.append(abs(arr[start] + arr[end - 1]))
    tmp.append(abs(arr[start + 1] + arr[end - 1]))
    min_choice = min(tmp)

    if min_choice == tmp[0]:
        return 0
    elif min_choice == tmp[1]:
        return 1
    else:
        return 2

def solve(N, arr):
    arr.sort()
    if arr[0]>0:
        return arr[0], arr[1]
    if arr[-1]<0:
        return arr[-2], arr[-1]

    start=0
    end=N-1
    x = arr[start]
    y = arr[end]
    result = abs(x+y)

    while start<end:
        if abs(arr[start]+arr[end])<result:
            x = arr[start]
            y = arr[end]
            result = abs(arr[start]+arr[end])

        select=choose(arr, start, end)

        if select == 0:
            start+=1
        elif select == 1:
            end-=1
        else:
            start+=1
            end-=1

    return x, y

if __name__=="__main__":
    N=int(input())
    arr=list(map(int, input().split()))
    x, y = solve(N, arr)
    print(x, y)