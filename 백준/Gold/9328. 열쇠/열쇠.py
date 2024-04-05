import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solve(arr, keys, h, w):
    visited = []
    for _ in range(h):
        visited.append([False for _ in range(w)])

    queue = deque()
    for y in range(h):
        for x in range(w):
            if y in (0, h - 1) or x in (0, w - 1):
                if arr[y][x] == '*':
                    continue
                visited[y][x] = True
                queue.append((y, x))

    upper_queue = []
    result = 0
    is_moved = True
    while is_moved:
        queue.extend(upper_queue)
        upper_queue = []
        is_moved = False

        while queue:
            y, x = queue.popleft()
            if arr[y][x] == "$":
                result += 1
            elif arr[y][x].isupper() and arr[y][x].lower() not in keys:
                upper_queue.append((y, x))
                continue
            elif arr[y][x].islower():
                keys.add(arr[y][x])
            is_moved = True

            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if not 0 <= ny < h or not 0 <= nx < w:
                    continue
                if visited[ny][nx]:
                    continue
                if arr[ny][nx] == "*":
                    continue
                queue.append((ny, nx))
                visited[ny][nx] = True

    return result


if __name__ == "__main__":
    for _ in range(int(input())):
        h, w = map(int, input().split())
        arr = []
        for _ in range(h):
            arr.append(list(input()))
        keys = set()
        possession_keys = input()
        if possession_keys != '0':
            for k in list(possession_keys):
                keys.add(k)

        print(solve(arr, keys, h, w))
