import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, tree):
    count=0
    for i in tree.keys():
        if len(tree[i]) == 1:
            count+=1
    if count%2==0:
        return count // 2
    else:
        return (count+1) // 2

if __name__ == '__main__':
    N = int(input())

    tree = {}

    for i in range(N):
        tree[i] = []

    for _ in range(N - 1):
        A, B = map(int, input().split())
        tree[A].append(B)
        tree[B].append(A)

    print(solve(N, tree))
