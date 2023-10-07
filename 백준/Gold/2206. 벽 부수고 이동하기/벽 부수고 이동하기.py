import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()
dy=[0,0,1,-1]
dx=[1,-1,0,0]

def BFS(matrix, row, column):
    queue=deque([(0,0,0)])
    matrix[0][0][0]=1
    while queue:
        y, x, is_broken = queue.popleft()
        if y == row - 1 and x == column - 1:  # 종료 검사
            return matrix[is_broken][y][x]
        for i in range(4):
            new_y, new_x = y+dy[i], x+dx[i]
            if 0<=new_y<row and 0<=new_x<column:
                if matrix[is_broken][new_y][new_x]==0:
                    matrix[is_broken][new_y][new_x]=matrix[is_broken][y][x]+1
                    queue.append((new_y, new_x, is_broken))
                elif matrix[is_broken][new_y][new_x]==-1:
                    if is_broken==1:
                        continue
                    else:
                        matrix[1][new_y][new_x]=matrix[0][y][x]+1
                        queue.append((new_y, new_x, 1))
    return -1

if __name__=="__main__":
    row, column = map(int, input().split())
    matrix=[[], []]
    for _ in range(row):
        temp=list(map(lambda x:-int(x), list(input())))
        matrix[0].append(temp[:])
        matrix[1].append(temp[:])
    print(BFS(matrix, row, column))