import sys
input = lambda: sys.stdin.readline().rstrip()


def solve(N, arr):
    answer = [-1 for _ in range(N)]
    stack = []
    index = 0
    for i in range(N):
        while stack and stack[-1][0] < arr[i]:
            _, idx = stack.pop()
            answer[idx] = arr[i]

        stack.append((arr[i], index))
        index += 1

    return answer


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    print(*solve(N, arr))
