a,b,c = map(int, input().split())
max_value = max(a,b,c)
sum_value = sum([a,b,c])
if max_value<sum_value-max_value:
    print(sum_value)
else:
    print((sum_value-max_value)*2-1)