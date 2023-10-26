import sys
sys.setrecursionlimit(10**5)
input = lambda:sys.stdin.readline().rstrip()
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def solve(y, x, matrix, dp, row, col):
    if dp[y][x] != -1:
        return dp[y][x]
    else:
        result = 0
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ny<0 or ny>=row or nx<0 or nx>=col:
                continue
            if matrix[ny][nx] <= matrix[y][x]:
                continue
            result+=solve(ny, nx, matrix, dp, row, col)
        dp[y][x] = result
        return dp[y][x]

if __name__=="__main__":
    M, N = map(int, input().split())
    matrix=[]
    for _ in range(M):
        matrix.append(list(map(int, input().split())))
    dp=[[-1 for _ in range(N)] for _ in range(M)]
    dp[0][0]=1
    print(solve(M-1, N-1, matrix, dp, M, N))