import sys
input = lambda:sys.stdin.readline().rstrip()


def solve(N, arr):
    answer = 0
    count = 0
    last = 0
    for n in arr+[0]:
        if n > last:
            count += 1
        else:
            answer += count*(count-1)//2
            count = 1
        last = n
    return answer + N


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    print(solve(N, arr))