import sys
input = lambda: sys.stdin.readline().rstrip()


def find(parent, a):
    if parent[a] == a:
        return a
    parent[a] = find(parent, parent[a])
    return parent[a]


def union(parent, a, b):
    a_parent = find(parent, a)
    b_parent = find(parent, b)
    if a_parent != b_parent:
        parent[b_parent] = a_parent



if __name__ == "__main__":
    n, m = map(int, input().split())
    parent = [i for i in range(n+1)]

    for _ in range(m):
        command, a, b = map(int, input().split())
        if command == 0:
            union(parent, a, b)
        elif command == 1:
            if find(parent, a) == find(parent, b):
                print("YES")
            else:
                print("NO")
