import sys

input = lambda: sys.stdin.readline().rstrip()
max_even_bishop = 0
max_odd_bishop = 0


def find_empty_square(board, N, is_even):
    squares = []
    for i in range(N):
        if is_even:
            for j in range(0, N, 2):
                if board[i][j] == 1:
                    squares.append((j, i))
            is_even = False
        else:
            for j in range(1, N, 2):
                if board[i][j] == 1:
                    squares.append((j, i))
            is_even = True
    return squares


def make_status(board, N, y, x, status):
    board[y][x] += status
    for i in range(1, N):
        if (x + i < N and y + i < N) and (board[y + i][x + i] != 0):
            board[y + i][x + i] += status
        if (x - i >= 0 and y + i < N) and (board[y + i][x - i] != 0):
            board[y + i][x - i] += status


def dfs(board, N, bishop, empty_squares, index, is_even):
    for i in range(index, len(empty_squares)):
        x, y = empty_squares[i]
        if board[y][x] != 1:
            continue
        make_status(board, N, y, x, 1)
        dfs(board, N, bishop + 1, empty_squares, i, is_even)
        make_status(board, N, y, x, -1)

    if is_even:
        global max_even_bishop
        max_even_bishop = max(max_even_bishop, bishop)
    else:
        global max_odd_bishop
        max_odd_bishop = max(max_odd_bishop, bishop)


if __name__ == "__main__":
    board = []
    N = int(input())
    for _ in range(N):
        board.append(list(map(int, input().split())))

    empty_squares = find_empty_square(board, N, True)
    dfs(board, N, 0, empty_squares, 0, True)

    empty_squares = find_empty_square(board, N, False)
    dfs(board, N, 0, empty_squares, 0, False)

    print(max_even_bishop + max_odd_bishop)