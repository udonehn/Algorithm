import sys
input = lambda:sys.stdin.readline().rstrip()

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def find_dirty_space(room, y, x):
    for i in range(4):
        if room[y+dy[i]][x+dx[i]] == 0:
            return True
    return False


def solve(y, x, d, room):
    count = 0
    while True:
        if room[y][x] == 0:
            count+=1
            room[y][x] = 2

        if find_dirty_space(room, y, x):
            d = (d + 3) % 4
            if room[y+dy[d]][x+dx[d]] == 0:
                x, y = x+dx[d], y+dy[d]
        else:
            if room[y-dy[d]][x-dx[d]] == 1:
                return count
            y = y-dy[d]
            x = x-dx[d]


if __name__ == "__main__":
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())

    room = []
    for _ in range(N):
        room.append(list(map(int, input().split())))

    print(solve(r, c, d, room))