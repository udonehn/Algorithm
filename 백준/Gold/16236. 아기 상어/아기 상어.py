import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def find_fish(space, N, level, baby_shark):
    arr = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i].append(space[i][j])

    candidate = []
    queue = deque([(0, baby_shark[0], baby_shark[1])])
    arr[baby_shark[0]][baby_shark[1]] = -1
    while queue:
        distance, y, x = queue.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
            if arr[ny][nx] == -1 or arr[ny][nx] > level:
                continue
            if arr[ny][nx] != 0 and arr[ny][nx] < level:
                candidate.append((distance+1, ny, nx))
            queue.append((distance+1, ny, nx))
            arr[ny][nx] = -1
    if candidate:
        return min(candidate)
    else:
        return -1, -1, -1


def solve(space, N):
    for i in range(N):
        for j in range(N):
            if space[i][j] == 9:
                baby_shark = (i, j) #행, 열
    level = 2
    time = 0
    number_of_ate_fish = 0
    while True:
        distance, fish_y, fish_x = find_fish(space, N, level, baby_shark)

        if distance == -1:
            return time

        time += distance
        space[baby_shark[0]][baby_shark[1]] = 0
        baby_shark = (fish_y, fish_x)
        number_of_ate_fish += 1
        if number_of_ate_fish == level:
            level += 1
            number_of_ate_fish = 0


if __name__ == "__main__":
    N = int(input())
    space = []
    for _ in range(N):
        space.append(list(map(int, input().split())))
    print(solve(space, N))
