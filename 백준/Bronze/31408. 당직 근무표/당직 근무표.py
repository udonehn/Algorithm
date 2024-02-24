import sys
input = lambda: sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    count = dict()
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    max_value = max(count.values())
    if max_value <= (N+1)//2:
        print("YES")
    else:
        print("NO")
