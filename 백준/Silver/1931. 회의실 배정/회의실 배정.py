if __name__ == "__main__":
    N = int(input())
    arr = []
    for _ in range(N):
        start, end = map(int, input().split())
        arr.append((end, start))
    arr.sort()
    last_time = 0
    count = 0
    for end, start in arr:
        if start >= last_time:
            count += 1
            last_time = end
    print(count)