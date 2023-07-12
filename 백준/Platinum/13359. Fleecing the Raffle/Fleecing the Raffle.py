import sys
input=lambda:sys.stdin.readline().rstrip()

n, p=map(int, input().split())

v=1/((n+1)*n)
i=2
dp=v
while True:
    dp=dp*(i/(i-1))*((n+i-p)/(n+i))
    if v>=dp:
        i-=1
        break
    v=dp
    i+=1

ans=1
for j in range(p-1):
    ans=ans*(n-j)/(n+i-j)
ans=ans*i*p/(n+i-p+1)

print(ans)