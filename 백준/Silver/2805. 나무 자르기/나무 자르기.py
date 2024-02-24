def check(mid, trees, M) -> bool:
    """충분한 나무가 된다면 T반환."""
    length = 0
    for tree in trees:
        if tree > mid:
            length += tree-mid
    if length >= M:
        return True
    else:
        return False


if __name__ == "__main__":
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))

    low = 0
    high = max(trees)

    while low+1 < high:
        mid = (low+high)//2
        if check(mid, trees, M):
            low = mid
        else:
            high = mid

    print(low)