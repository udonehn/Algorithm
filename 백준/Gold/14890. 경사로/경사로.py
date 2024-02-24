import sys
input = lambda: sys.stdin.readline().rstrip()


def isPossible(N, L, road):
    last = road[0]
    count = 1
    i = 1
    while i < N:
        if road[i] == last:
            count += 1
            i += 1
        elif road[i] < last:
            for j in range(L):
                if i + j >= N or last - road[i + j] != 1:
                    return False
            count = 0
            last -= 1
            i += L
        elif road[i] > last:
            if road[i] - last != 1:
                return False
            if count < L:
                return False
            count = 1
            last = road[i]
            i += 1

    return True

def solve(N, L, arr):
    count = 0
    for i in range(N):
        road = []
        for j in arr[i]:
            road.append(j)
        if isPossible(N, L, road):
            count += 1

        road = []
        for j in range(N):
            road.append(arr[j][i])
        if isPossible(N, L, road):
            count += 1
    return count


if __name__ == "__main__":
    N, L = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    print(solve(N, L, arr))
