import sys

input = lambda: sys.stdin.readline().rstrip()


def make_false(sq, arr, start, end):
    if start%sq==0:
        i=start//sq
    else:
        i=start//sq+1
        
    while True:
        tmp = sq * i
        if tmp > end:
            break
        arr[tmp - start] = False
        i += 1


if __name__ == "__main__":
    start, end = map(int, input().split())
    arr = [True for _ in range(end - start + 1)]
    i = 2
    while True:
        sq = i ** 2
        if sq > end:
            break
        make_false(sq, arr, start, end)
        i += 1

    count = 0
    for i in range(end - start + 1):
        if arr[i]:
            count += 1

    print(count)