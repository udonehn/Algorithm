import sys
input = lambda: sys.stdin.readline().rstrip()


def check_distance(selected_chicken, house):
    distance=0

    for i in range(len(house)):
        each_distance=sys.maxsize
        for chicken_row, chicken_col in selected_chicken:
            each_distance=min(each_distance, abs(chicken_row-house[i][0])+abs(chicken_col-house[i][1]))
        distance+=each_distance

    return distance

def solve(N, M, house, chicken, min_distance, index, stack):
    if len(stack)==M:
        return check_distance(stack, house)
    for i in range(index, len(chicken)):
        min_distance = min(min_distance, solve(N, M, house, chicken, min_distance, i+1, stack+[chicken[i]]))

    return min_distance


if __name__=="__main__":
    N, M = map(int, input().split())
    house=[]
    chicken=[]
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(N):
            if row[j]==1:
                house.append((i,j))
            elif row[j]==2:
                chicken.append((i,j))

    print(solve(N, M, house, chicken, sys.maxsize, 0, []))