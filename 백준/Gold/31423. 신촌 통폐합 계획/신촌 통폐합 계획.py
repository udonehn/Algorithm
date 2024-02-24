import sys
input = lambda: sys.stdin.readline().rstrip()


def dfs(index, graph, arr):
    stack = [index]
    while stack:
        node = stack.pop()
        print(arr[node], end='')
        stack.extend(graph[node])


if __name__ == "__main__":
    N = int(input())
    arr = ['']
    for _ in range(N):
        arr.append(input())

    graph = [[] for _ in range(N+1)]
    for _ in range(N - 1):
        i, j = map(int, input().split())
        graph[i].append(j)
    for index in range(N+1):
        graph[index].reverse()

    dfs(i, graph, arr)
