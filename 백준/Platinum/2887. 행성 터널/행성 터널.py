import sys
from heapq import heappush, heappop
sys.setrecursionlimit(1000000)
input = lambda: sys.stdin.readline().rstrip()


def find(parent, a):
    if parent[a] == a:
        return a
    parent[a] = find(parent, parent[a])
    return parent[a]


def solve(N, arr):
    xyz = [[(0, 0) for _ in range(N)] for _ in range(3)]
    for i in range(3):
        for j in range(N):
            xyz[i][j] = (arr[j][i], j)
        xyz[i].sort()

    heap = []
    for i in range(3):
        for j in range(N - 1):
            heappush(heap, (abs(xyz[i][j][0] - xyz[i][j+1][0]), xyz[i][j][1], xyz[i][j+1][1]))

    parent = [i for i in range(N)]
    answer = 0
    while heap:
        cost, a, b = heappop(heap)
        a_parent = find(parent, a)
        b_parent = find(parent, b)
        if a_parent != b_parent:
            parent[a_parent] = b_parent
            answer += cost

    return answer


if __name__ == "__main__":
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    print(solve(N, arr))
