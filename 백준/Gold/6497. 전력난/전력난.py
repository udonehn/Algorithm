import sys
sys.setrecursionlimit(1000000)
input = lambda: sys.stdin.readline().rstrip()


def find(parent, a):
    if parent[a] == a:
        return a
    parent[a] = find(parent, parent[a])
    return parent[a]


def solve(m, n, edges):
    """Kruskal's MST Algorithm"""
    parent = [i for i in range(m)]
    edges.sort(key=lambda x: x[2])
    save = 0
    max_cost = 0
    for a, b, cost in edges:
        max_cost += cost
        a_parent = find(parent, a)
        b_parent = find(parent, b)
        if a_parent != b_parent:
            parent[a_parent] = b_parent
            save += cost

    return max_cost - save


if __name__ == "__main__":
    while True:
        case = input()
        if case == "0 0":
            break
        m, n = map(int, case.split())
        edges = []
        for _ in range(n):
            edges.append(tuple(map(int, input().split())))

        print(solve(m, n, edges))

