def solve(maze, N, M):
    for i in range(1, N+1):
        for j in range(1, M+1):
            maze[i][j] = maze[i][j] + max(maze[i-1][j], maze[i][j-1])

    return maze[N][M]


if __name__ == "__main__":
    N, M = map(int, input().split())
    maze = [[0 for _ in range(M+1)]]
    for _ in range(N):
        maze.append([0] + list(map(int, input().split())))

    print(solve(maze, N, M))