while True:
    N=input()
    if N=='0 0':
        break
    A,B=map(int, N.split())
    if A>B:
        print("Yes")
    else:
        print("No")