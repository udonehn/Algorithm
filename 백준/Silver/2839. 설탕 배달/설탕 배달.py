N = int(input())
five = N//5
r = N%5

if r == 1:
    if five<1:
        print(-1)
    else:
        print(five+1)
elif r == 2:
    if five<2:
        print(-1)
    else:
        print(five+2)
elif r == 3:
    print(five+1)
elif r == 4:
    if five<1:
        print(-1)
    else:
        print(five+2)
else:
    print(five)