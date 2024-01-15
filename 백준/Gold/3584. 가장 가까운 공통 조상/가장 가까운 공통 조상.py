import sys
input = lambda:sys.stdin.readline().rstrip()

def check_finished(visited):
    for node in visited[1:]:
        if not node:
            return False
    return True

def find_root(n, graph):
    for start in range(1, n+1):
        visited=[False for _ in range(n+1)]
        stack=[start]
        visited[start] = True
        while stack:
            node = stack.pop()
            for next_node in graph[node]:
                if not visited[next_node]:
                    visited[next_node]=True
                    stack.append(next_node)

        if check_finished(visited):
            return start

def find_path(n, graph, root, node1):
    visited = [False for _ in range(n + 1)]
    stack=[(root,[root])]
    while stack:
        node, path = stack.pop()
        if node == node1:
            return path+[node]
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append((next_node, path+[next_node]))


def solve(n, graph, node1, node2):
    root = find_root(n, graph)
    for i in range(1, N+1):
        for node in graph[i]:
            graph[node].append(i)
    node1_path = find_path(n, graph, root, node1)
    node2_path = find_path(n, graph, root, node2)

    answer=-1
    for node in node1_path:
        if node in node2_path:
            answer=node

    return answer

if __name__=="__main__":
    for _ in range(int(input())):
        N = int(input())
        graph=dict()
        for i in range(1, N+1):
            graph[i]=[]
        for _ in range(N-1):
            A, B = map(int, input().split())
            graph[A].append(B)
        node1, node2 = map(int, input().split())
        print(solve(N, graph, node1, node2))