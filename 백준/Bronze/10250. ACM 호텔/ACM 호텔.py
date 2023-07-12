for _ in range(int(input())):
    H, W, N = map(int, input().split())
    if N%H!=0:
        XX=str(N//H+1)
        YY=str(N%H)
    else:
        XX=str(N//H)
        YY=str(H)
    if len(XX)==1:
        XX='0'+XX
    print(YY+XX)