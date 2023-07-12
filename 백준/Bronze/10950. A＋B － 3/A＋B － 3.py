A = int(input())

s = ''
for i in range(A):
    a, b = map(int, input().split())
    s += str(a+b)+'\n'

print(s)