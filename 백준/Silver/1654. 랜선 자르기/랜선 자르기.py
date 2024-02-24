def check(N, arr, mid):
    result = 0
    for cable in arr:
        result += cable//mid
    if result >= N:  # 적절하거나 짧음 -> 길이를 늘려야 함
        return True
    else:   # 너무 길음 -> 길이를 줄여야 함
        return False


def solve(N, arr):
    low = 1
    high = max(arr)

    while low <= high:
        mid = (low + high) // 2
        if check(N, arr, mid):
            low = mid + 1
        else:
            high = mid - 1

    return high


if __name__ == "__main__":
    K, N = map(int, input().split())
    arr = []
    for _ in range(K):
        arr.append(int(input()))

    print(solve(N, arr))
