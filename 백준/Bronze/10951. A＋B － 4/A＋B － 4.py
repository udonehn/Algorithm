s = ''
while True:
    try:
        a, b = map(int, input().split())
        s += str(a+b)+'\n'
    except:
        break

print(s)