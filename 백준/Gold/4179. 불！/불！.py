import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solve(R, C, maze):
    queue = deque()
    for row in range(R):
        for col in range(C):
            if maze[row][col] == "F":
                maze[row][col] = 1
                queue.append((row, col, 1))
            if maze[row][col] == "J":
                jihun = (row, col)
                maze[row][col] = 0
            if maze[row][col] == ".":
                maze[row][col] = 0

    while queue:
        y, x, count = queue.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny < 0 or ny >= R or nx < 0 or nx >= C:
                continue
            if maze[ny][nx] == "#" or (maze[ny][nx] <= count+1 and maze[ny][nx] != 0):
                continue
            maze[ny][nx] = count + 1
            queue.append((ny, nx, count+1))

    maze[jihun[0]][jihun[1]] = -1
    queue = deque([(jihun[0], jihun[1], -1)])

    while queue:
        y, x, count = queue.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny < 0 or ny >= R or nx < 0 or nx >= C:
                return -count
            if maze[ny][nx] == "#" or (0 > maze[ny][nx] >= count-1) or (0 < maze[ny][nx] <= -(count-1)):
                continue
            maze[ny][nx] = count - 1
            queue.append((ny, nx, count - 1))

    return "IMPOSSIBLE"


if __name__ == "__main__":
    R, C = map(int, input().split())
    maze = []
    for _ in range(R):
        maze.append(list(input()))
    print(solve(R, C, maze))
