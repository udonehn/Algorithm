import sys
input = lambda:sys.stdin.readline().rstrip()

def solve(N, arr):
    answer = 1
    arr.sort()

    current_i = arr[0][1]
    for r, i in arr[1:]:
        if i < current_i:
            current_i = i
            answer += 1
    return answer


if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        arr = []
        for _ in range(N):
            r, i = map(int, input().split())
            arr.append((r, i))
        print(solve(N, arr))
