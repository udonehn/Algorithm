import sys
input = lambda: sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())
    d = dict()
    for t in input().split():
        if t in d:
            d[t] += 1
        else:
            d[t] = 1
    H = input()
    if H in d:
        print(d[H])
    else:
        print(0)
