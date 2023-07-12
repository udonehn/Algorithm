T=int(input())
for _ in range(T):
    N=int(input())
    p=[0,1,1,1,2,2]
    if N<6:
        print(p[N])
    else:
        j=1
        for i in range(6,N+1):
            p.append(p[i-1]+p[i-5])
        print(p[N])