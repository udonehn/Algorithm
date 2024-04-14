input()
A = set(input().split())
B = set(input().split())
print(len(B - A) + len(A - B))
