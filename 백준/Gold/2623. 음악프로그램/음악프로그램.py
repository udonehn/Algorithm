import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()


def solve(N, M, arr):
    graph = dict()
    in_degree = [0 for _ in range(N + 1)]
    for i in range(1, N + 1):
        graph[i] = set()
    for s in arr:
        for i in range(1, s[0]):
            start = s[i]
            end = s[i + 1]
            if end not in graph[start]:
                graph[start].add(end)
                in_degree[end] += 1

    queue = deque()
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            queue.append(i)

    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for next_node in graph[node]:
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                queue.append(next_node)

    if sum(in_degree) != 0:
        return [0]
    return result


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = []
    for _ in range(M):
        arr.append(list(map(int, input().split())))
    for n in solve(N, M, arr):
        print(n)
