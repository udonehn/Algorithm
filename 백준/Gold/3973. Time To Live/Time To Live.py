import sys
input = lambda: sys.stdin.readline().rstrip()


def find_leaf(tree):
    ROOT = 1
    visited = [False] * 100001
    visited[ROOT] = True
    
    stack = [(ROOT, 0)]
    leaf = []
    while stack:
        p, length = stack.pop()
        count = 0
        for i in tree[p]:
            node = i
            if not visited[node]:
                count += 1
                visited[node] = True
                stack.append((node, length+1))
        if count == 0:
            leaf.append((length, p))

    return leaf


def DFS(start, tree):
    stack = [(start, 0)]
    visited = [False] * 100001
    visited[start] = True
    
    answer = 0
    while stack:
        p, length = stack.pop()
        count = 0
        for i in tree[p]:
            node = i
            if not visited[node]:
                count += 1
                visited[node] = True
                stack.append((node, length+1))
        if count == 0:
            answer = max(answer, length)
    return answer


def solve(N, tree):
    leaf = find_leaf(tree)
    leaf.sort(reverse=True)
    answer = DFS(leaf[0][1], tree)
    if answer % 2 == 0:
        return answer // 2
    else:
        return answer // 2 + 1

if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())

        tree = {}
        for i in range(N):
            tree[i]=[]

        for _ in range(N-1):
            A, B = map(int, input().split())
            tree[A].append(B)
            tree[B].append(A)

        print(solve(N, tree))