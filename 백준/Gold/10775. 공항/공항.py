import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()


def find(parent, n):
    if parent[n] == n:
        return n
    parent[n] = find(parent, parent[n])
    return parent[n]


def solve(G, P, arr):
    result = 0
    parent = [i for i in range(G + 1)]
    for n in arr:
        n_parent = find(parent, n)
        if n_parent == 0:
            break
        parent[n_parent] = n_parent - 1
        result += 1
    return result


if __name__ == "__main__":
    G = int(input())
    P = int(input())
    arr = []
    for _ in range(P):
        arr.append(int(input()))
    print(solve(G, P, arr))
