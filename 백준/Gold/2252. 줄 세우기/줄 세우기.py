import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()


def solve(N, M, arr):
    in_degree = [0 for _ in range(N + 1)]
    graph = dict()
    for i in range(1, N + 1):
        graph[i] = []
    for s, e in arr:
        graph[s].append(e)
        in_degree[e] += 1

    queue = deque()
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            queue.append(i)

    answer = []
    while queue:
        node = queue.popleft()
        answer.append(node)
        for next_node in graph[node]:
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                queue.append(next_node)
    return answer


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = []
    for _ in range(M):
        arr.append(list(map(int, input().split())))
    print(*solve(N, M, arr))
