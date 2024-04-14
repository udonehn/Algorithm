import sys
input = lambda: sys.stdin.readline().rstrip()


def dfs(visited, arr, y, x):
    path = [(y, x)]
    while True:
        y, x = path[-1]

        if arr[y][x] == 'U':
            ny, nx = y - 1, x
        elif arr[y][x] == 'D':
            ny, nx = y + 1, x
        elif arr[y][x] == 'L':
            ny, nx = y, x - 1
        elif arr[y][x] == 'R':
            ny, nx = y, x + 1

        if visited[ny][nx]:
            result = 0
            break
        elif(ny, nx) in path:
            result = 1
            break

        path.append((ny, nx))

    for y, x in path:
        visited[y][x] = True
    return result


def solve(N, M, arr):
    visited = [[False for _ in range(M)] for _ in range(N)]
    answer = 0
    for y in range(N):
        for x in range(M):
            if not visited[y][x]:
                answer += dfs(visited, arr, y, x)
    return answer


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(input()))
    print(solve(N, M, arr))
