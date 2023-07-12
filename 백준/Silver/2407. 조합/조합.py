n,m=map(int,input().split())
a,b=1,1
for i in range(m):
    a=a*(n-i)
    b=b*(i+1)
print(a//b)