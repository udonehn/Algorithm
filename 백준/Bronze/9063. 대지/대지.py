N = int(input())
x_max = -10000
x_min = 10000
y_max = -10000
y_min = 10000

if N<2:
    print(0)
else:
    for _ in range(N):
        x, y = map(int, input().split())
        x_max = max(x, x_max)
        x_min = min(x, x_min)
        y_max = max(y, y_max)
        y_min = min(y, y_min)

    print((x_max-x_min)*(y_max-y_min))