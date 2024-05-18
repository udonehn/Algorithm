import sys
input = lambda: sys.stdin.readline().rstrip()


def solve(N, arr):
    arr.sort()
    answer = [0, 0, 0]
    answer_size = sys.maxsize

    for i in range(N-2):
        start = i + 1
        end = N - 1
        while start < end:
            s = arr[i] + arr[start] + arr[end]
            if abs(s) < answer_size:
                answer_size = abs(s)
                answer = [arr[i], arr[start], arr[end]]
            if s < 0:
                start += 1
            elif s > 0:
                end -= 1
            else:
                return answer

    return answer


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))

    print(*solve(N, arr))
