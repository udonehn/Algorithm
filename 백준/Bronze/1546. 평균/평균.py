a = int(input())

b = list(map(int, input().split()))

max = max(b)
n=0

for i in range(a):
    n+=b[i]/max*100

print(n/a)