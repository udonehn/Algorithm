import sys
input = lambda: sys.stdin.readline().rstrip()


def find(parent, a):
    if parent[a] == a:
        return a
    parent[a] = find(parent, parent[a])
    return parent[a]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a != b:
        parent[a] = b


def solve(N, M, truth, parties):
    parent = [i for i in range(N + 1)]

    for i in range(len(truth) - 1):
        union(parent, truth[i], truth[i+1])

    for party in parties:
        for i in range(len(party)-1):
            union(parent, party[i], party[i+1])

    count = 0
    for party in parties:
        if not truth or find(parent, truth[0]) != find(parent, party[0]):
            count += 1
    return count


if __name__ == "__main__":
    N, M = map(int, input().split())
    truth = list(map(int, input().split()))[1:]
    parties = []
    for _ in range(M):
        parties.append(list(map(int, input().split()))[1:])
    print(solve(N, M, truth, parties))
