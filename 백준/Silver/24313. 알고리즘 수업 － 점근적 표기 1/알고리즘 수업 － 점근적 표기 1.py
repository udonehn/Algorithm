import sys
input = lambda: sys.stdin.readline().rstrip()


def solve(a1, a0, c, n0):
    if (a1 * n0 + a0 <= c * n0) and (a1 <= c):
        return 1
    else:
        return 0


if __name__ == "__main__":
    a1, a0 = map(int, input().split())
    c = int(input())
    n0 = int(input())
    print(solve(a1, a0, c, n0))
