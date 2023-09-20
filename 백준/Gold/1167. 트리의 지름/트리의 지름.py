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
            node = i[0]
            node_length = i[1]
            if not visited[node]:
                count += 1
                visited[node] = True
                stack.append((node, length+node_length))
        if count == 0:
            leaf.append((length, p))

    return sorted(leaf, reverse=True)


def DFS(start, tree):
    stack = [(start, 0)]
    visited = [False] * 100001
    visited[start] = True
    
    answer = 0
    while stack:
        p, length = stack.pop()
        count = 0
        for i in tree[p]:
            node = i[0]
            node_length = i[1]
            if not visited[node]:
                count += 1
                visited[node] = True
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
        tree[i]=[]

    for _ in range(N):
        input_list = list(map(int, input().split()))

        node = input_list[0]

        i = 1
        while input_list[i]!=-1:
            linked_node = input_list[i]
            length = input_list[i+1]
            tree[node].append((linked_node, length))
            tree[linked_node].append((node, length))
            i+=2

    print(solve(N, tree))
