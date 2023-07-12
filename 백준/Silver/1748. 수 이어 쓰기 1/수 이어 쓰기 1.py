import sys
N = int(sys.stdin.readline())
ans=0
n=''
if N<10:
    ans=N
else:
    for i in range(len(str(N))-1):
        n='9'
        for j in range(i):
            n+=str(0)
        ans+=int(n)*(i+1)
    nine=''
    for i in range(len(str(N))-1):
        nine+='9'
    ans+=(len(str(N)))*(N-int(nine))
print(ans)