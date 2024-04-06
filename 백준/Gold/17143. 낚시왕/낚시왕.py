import sys
input = lambda: sys.stdin.readline().rstrip()


R, C, M = map(int, input().split())
shark = []
for _ in range(M):
    shark.append(list(map(int, input().split())))
arr = [[[] for _ in range(C + 1)] for _ in range(R + 1)]
for r, c, s, d, z in shark:
    arr[r][c].append((s, d, z))
answer = 0
for man in range(1, C + 1):
    for row in range(R + 1):
        if arr[row][man]:
            _, _, size = arr[row][man].pop()
            answer += size
            break
    new_arr = [[[] for _ in range(C + 1)] for _ in range(R + 1)]
    for y in range(R + 1):
        for x in range(C + 1):
            if arr[y][x]:
                ny, nx = y, x
                s, d, z = arr[y][x][0]
                for _ in range(s):
                    if d == 1:
                        if ny == 1:
                            ny = 2
                            d = 2
                        else:
                            ny -= 1
                    elif d == 2:
                        if ny == R:
                            ny = R - 1
                            d = 1
                        else:
                            ny += 1
                    elif d == 3:
                        if nx == C:
                            nx = C - 1
                            d = 4
                        else:
                            nx += 1
                    elif d == 4:
                        if nx == 1:
                            nx = 2
                            d = 3
                        else:
                            nx -= 1
                new_arr[ny][nx].append((s, d, z))
    arr = new_arr

    for y in range(R + 1):
        for x in range(C + 1):
            if len(arr[y][x]) > 1:
                max_s, max_d, max_z = arr[y][x].pop()
                while arr[y][x]:
                    s, d, z = arr[y][x].pop()
                    if z > max_z:
                        max_s, max_d, max_z = s, d, z
                arr[y][x].append((max_s, max_d, max_z))

print(answer)
