H, M = map(int, input().split())

if(M<45):
    H-=1
    M=60+M-45
else:
    M=M-45

if(H==-1):
    H=23

print(H, M)