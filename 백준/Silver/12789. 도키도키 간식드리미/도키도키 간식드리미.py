import sys
input = lambda: sys.stdin.readline().rstrip()


def solve(N, arr):
    stack = []
    ticket = 1
    for num in arr:
        if num == ticket:
            ticket += 1
        else:
            stack.append(num)
        while stack:
            if stack[-1] == ticket:
                stack.pop()
                ticket += 1
            else:
                break
    if not stack:
        return "Nice"
    else:
        return "Sad"


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    print(solve(N, arr))
