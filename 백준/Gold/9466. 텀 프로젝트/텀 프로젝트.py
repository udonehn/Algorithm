import sys
sys.setrecursionlimit(1000000)
input = lambda: sys.stdin.readline().rstrip()


def dfs(graph, visited, path, node):
    path.append(node)
    visited[node] = True
    next_node = graph[node]

    if visited[next_node]:
        for i in range(len(path)):
            if path[i] == next_node:
                return len(path) - i
        return 0
    
    return dfs(graph, visited, path, next_node)


def solve(N, arr):
    visited = [True] + [False for _ in range(N)]
    answer = 0
    for i in range(1, N+1):
        if not visited[i]:
            answer += dfs(arr, visited, [], i)
    return N - answer


if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        arr = [-1] + list(map(int, input().split()))
        print(solve(N, arr))
