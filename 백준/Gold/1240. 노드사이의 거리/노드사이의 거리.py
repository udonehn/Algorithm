import sys
input = lambda : sys.stdin.readline().rstrip()

def dfs(tree, start, goal):
    visited = [False] * (len(tree)+2)
    stack=[(start, 0)]

    visited[start] = True

    while stack:
        node, distance_sum = stack.pop()
        for new_node, distance in tree[node]:
            if new_node == goal:
                return distance_sum+distance
            if not visited[new_node]:
                stack.append((new_node, distance_sum+distance))
                visited[node] = True


if __name__=="__main__":
    N, M = map(int, input().split())
    tree={}
    for i in range(1,N+1):
        tree[i]=[]
    for _ in range(N-1):
        A, B, distance = map(int, input().split())
        tree[A].append((B, distance))
        tree[B].append((A, distance))

    for _ in range(M):
        A, B = map(int, input().split())
        print(dfs(tree, A, B))
        