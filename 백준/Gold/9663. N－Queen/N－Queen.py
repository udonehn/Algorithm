import sys
input = lambda : sys.stdin.readline().rstrip()
count = 0

def make_available_or_not(N, chess, y, x, stat):
    for i in range(N):
        chess[i][x] += stat
        chess[y][i] += stat
        if y-i>=0 and x-i>=0:
            chess[y-i][x-i] += stat
        if y-i>=0 and x+i<N:
            chess[y-i][x+i] += stat
        if y+i<N and x+i<N:
            chess[y+i][x+i] += stat
        if y+i<N and x-i>=0:
            chess[y+i][x-i] += stat

def solve(N, chess, level):
    global count
    if level == N:
        count+=1
        return

    for i in range(N):
        if chess[level][i]==0:
            make_available_or_not(N, chess, level, i, 1)
            solve(N, chess, level+1)
            make_available_or_not(N, chess, level, i, -1)

if __name__ == "__main__":
    N=int(input())
    chess = [[0 for _ in range(N)] for _ in range(N)]
    solve(N, chess, 0)
    print(count)