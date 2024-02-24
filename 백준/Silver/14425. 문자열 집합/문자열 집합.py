import sys
input = lambda: sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N, M = map(int, input().split())
    s = set()
    for _ in range(N):
        s.add(input())
    count = 0
    for _ in range(M):
        if input() in s:
            count += 1
    print(count)
    