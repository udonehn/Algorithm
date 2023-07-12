x, y = map(int, input().split())
xset=set()
yset=set()
i=1
while True:
    if x%i==0:
        xset.add(x/i)
    if y%i==0:
        yset.add(y/i)
    if i>x and i>y:
        if xset&yset:
            print(int(max(xset&yset)))
        else:
            print(1)
        break
    i+=1
xxset=set()
yyset=set()
i=1
if x == y:
    print(x)
else:
    while True:
        if xxset&yyset:
            print(list(xxset&yyset)[0])
            break
        else:
            xxset.add(x*i)
            yyset.add(y*i)
        i+=1