import sys
sys.setrecursionlimit(10000000)
input = lambda: sys.stdin.readline().rstrip()


def find(parent, a):
    if parent[a] == a:
        return a
    parent[a] = find(parent, parent[a])
    return parent[a]


def solve(n, m, game):
    parent = [i for i in range(n)]
    count = 1
    for a, b in game:
        a_parent = find(parent, a)
        b_parent = find(parent, b)
        if a_parent == b_parent:
            return count
        parent[a_parent] = b_parent
        count += 1
    return 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    game = []
    for _ in range(m):
        game.append(list(map(int, input().split())))
    print(solve(n, m, game))
