import sys
import itertools
input=lambda:sys.stdin.readline().rstrip()
ans=[]

def DFS(arr,n,m):
    if len(arr)==m:
        ans.append(' '.join(arr))
        return
    else:
        for i in range(1, n+1):
            if str(i) not in arr:
                DFS(arr+[str(i)],n,m)


n,m=map(int, input().split())

DFS([],n,m)

print('\n'.join(ans))