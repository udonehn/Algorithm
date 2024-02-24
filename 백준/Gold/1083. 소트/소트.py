import sys
input = lambda: sys.stdin.readline().rstrip()


def get_available_numbers(arr, N, index, S):
    result = (0, -1)
    for i in range(index, N):
        if i-index <= S and arr[i] >= result[0]:
            result = (arr[i], i)
    return result


def switch(arr, index, target_index):
    for i in range(target_index, index, -1):
        arr[i], arr[i-1] = arr[i-1], arr[i]


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    S = int(input())

    for index in range(N):
        _, target_index, = get_available_numbers(arr, N, index, S)
        if target_index == -1:
            continue
        switch(arr, index, target_index)
        S = S - (target_index-index)

    print(*arr)
