import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def bfs(arr, N, M, visited, y, x):
    queue = deque([(y, x)])
    visited[y][x] = True
    visited_list = []
    count = 0
    while queue:
        y, x = queue.popleft()
        count += 1
        visited_list.append((y, x))
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i],
            if not 0 <= ny < N or not 0 <= nx < M:
                continue
            if arr[ny][nx] == 1:
                continue
            if visited[ny][nx]:
                continue
            visited[ny][nx] = True
            queue.append((ny, nx))
    return visited_list, count


def solve(N, M, arr):
    visited = []
    area = []
    answer = []

    for y in range(N):
        visited.append([False for _ in range(M)])
        area.append([0 for _ in range(M)])
        answer.append([0 for _ in range(M)])

    number = 0
    for y in range(N):
        for x in range(M):
            if arr[y][x] == 0 and not visited[y][x]:
                visited_list, size = bfs(arr, N, M, visited, y, x)
                for visited_y, visited_x in visited_list:
                    area[visited_y][visited_x] = (size, number)
                number += 1

    for y in range(N):
        for x in range(M):
            if arr[y][x] == 1:
                count = 1
                number_set = set()
                for i in range(4):
                    ny, nx = y+dy[i], x+dx[i]
                    if not 0 <= ny < N or not 0 <= nx < M:
                        continue
                    if arr[ny][nx] == 1:
                        continue
                    size, number = area[ny][nx]
                    if number not in number_set:
                        count += size
                        number_set.add(number)
                answer[y][x] = count

    for y in range(N):
        for x in range(M):
            print(answer[y][x] % 10, end='')
        print()


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, list(input()))))

    solve(N, M, arr)
