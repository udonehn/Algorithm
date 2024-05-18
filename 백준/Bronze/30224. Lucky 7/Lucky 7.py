N = int(input())
if '7' not in list(str(N)):
    if N % 7 != 0:
        print(0)
    else:
        print(1)
else:
    if N % 7 != 0:
        print(2)
    else:
        print(3)