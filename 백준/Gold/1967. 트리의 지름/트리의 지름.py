import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()


def find_leaf(tree):
    ROOT = 1
    visited = [ROOT]
    stack = [(ROOT, 0)]
    leaf = []
    while stack:
        p, length = stack.pop()
        count = 0
        for i in tree[p]:
            node = i[0]
            node_length = i[1]
            if node not in visited:
                count += 1
                visited.append(node)
                stack.append((node, length+node_length))
        if count == 0:
            leaf.append((length, p))

    return sorted(leaf, reverse=True)


def DFS(start, tree):
    stack = [(start, 0)]
    visited = [start]
    answer = 0
    while stack:
        p, length = stack.pop()
        count = 0
        for i in tree[p]:
            node = i[0]
            node_length = i[1]
            if node not in visited:
                count += 1
                visited.append(node)
                stack.append((node, length+node_length))
        if count == 0:
            answer = max(answer, length)
    return answer


def solve(N, tree):
    leaf = find_leaf(tree)
    answer = DFS(leaf[0][1], tree)
    return answer

if __name__ == '__main__':
    N = int(input())

    tree = {}

    for i in range(N+1):
        tree[i] = []

    for _ in range(N - 1):
        A, B, length = map(int, input().split())
        tree[A].append((B, length))
        tree[B].append((A, length))

    print(solve(N, tree))
