def pec(n):
    ans=1
    if n>1:
        for i in range(n,0,-1):
            ans*=i
    return ans
N = int(input())
ans=0
for i in range(int(N/2)+1):
    t=i
    o=N-t*2
    ans+=pec(t+o)//(pec(t)*pec(o))

print(int(ans%10007))