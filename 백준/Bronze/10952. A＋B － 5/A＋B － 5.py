s = ''
while True:
    a, b = map(int, input().split())
    if(a==0 and b==0):
        break
    s += str(a+b)+'\n'
print(s)