import sys
input = lambda: sys.stdin.readline().rstrip()


def fibo(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    return fibo(N-1) + fibo(N-2)


if __name__ == "__main__":
    print(fibo(int(input())))
