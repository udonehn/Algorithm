input()
s = set(input().split())
input()
for i in input().split():
    if i in s:
        print(1, end=" ")
    else:
        print(0, end=" ")
