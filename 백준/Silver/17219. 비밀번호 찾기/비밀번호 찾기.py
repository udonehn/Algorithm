N, M = map(int, input().split())
pw = dict()
for _ in range(N):
    site, password = input().split()
    pw[site]=password
for _ in range(M):
    print(pw[input()])