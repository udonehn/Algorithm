import sys
input = lambda : sys.stdin.readline().rstrip()

def Z(start, level, number, ans):
    if start[1] == ans[1] and start[0] == ans[0]:
        print(number + 1)
        exit()

    next_down = start[0]+2**(level-1)
    next_right = start[1]+2**(level-1)

    if ans[0]<next_down and ans[1]<next_right:
        Z((start[0], start[1]), level-1, number, ans)
    elif ans[0]>=next_down and ans[1]<next_right:
        Z((next_down, start[1]), level - 1, number+(4**(level-1))*1, ans)
    elif ans[0]<next_down and ans[1]>=next_right:
        Z((start[0], next_right), level - 1, number+(4**(level-1))*2, ans)
    elif ans[0]>=next_down and ans[1]>=next_right:
        Z((next_down, next_right), level - 1, number+(4**(level-1))*3, ans)

    return number

if __name__ == "__main__":
    N, c, r = map(int, input().split())
    Z((0, 0), N, -1, (r, c))
