import sys
input = lambda: sys.stdin.readline().rstrip()


def calculate(arr):
    if not arr:
        return 0
    result = 0
    for i in range(0, len(arr), 2):
        if arr[i] == 1 or arr[i+1] == 1:
            # 1과는 곱하는 것보다 더하는 게 더 크다.
            result += arr[i]+arr[i+1]
        else:
            result += arr[i]*arr[i+1]
    return result


def solve(N, arr):
    arr.sort()
    minus = []
    zero = False
    i = 0
    for i in range(N):
        if arr[i] < 0:
            minus.append(arr[i])
        elif arr[i] == 0:
            zero = True
            i += 1
            break
        else:
            break

    plus = []
    for j in range(i, N):
        if arr[j] > 0:
            plus.append(arr[j])
    plus.reverse()

    minus_len = len(minus)
    plus_len = len(plus)
    result = 0

    if minus_len % 2 == 1:
        if not zero:
            result = minus[-1]
        minus = minus[:-1]

    if plus_len % 2 == 0:
        result += calculate(minus)
        result += calculate(plus)

    elif plus_len % 2 == 1:
        result += plus[-1]
        plus = plus[:-1]
        result += calculate(minus)
        result += calculate(plus)

    return result



if __name__ == "__main__":
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    print(solve(N, arr))