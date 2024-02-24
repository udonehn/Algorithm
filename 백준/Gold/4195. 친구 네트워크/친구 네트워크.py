import sys
input = lambda: sys.stdin.readline().rstrip()


def find(parent, a):
    if parent[a] == a:
        return a
    parent[a] = find(parent, parent[a])
    return parent[a]


def solve(friends):
    parent = dict()
    count = dict()
    for a, b in friends:
        if a not in parent and b in parent:
            parent[a] = b
            count[find(parent, b)] += 1
        elif b not in parent and a in parent:
            parent[b] = a
            count[find(parent, a)] += 1
        elif a not in parent and b not in parent:
            parent[a] = b
            parent[b] = b
            count[b] = 2
        elif a in parent and b in parent:
            a_root = find(parent, a)
            b_root = find(parent, b)
            if a_root != b_root:
                parent[a_root] = b_root
                count[b_root] += count[a_root]

        print(count[find(parent, a)])


if __name__ == "__main__":
    for _ in range(int(input())):
        friends = []
        for _ in range(int(input())):
            friends.append(input().split())
        solve(friends)
