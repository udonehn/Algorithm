ans=[]

def DFS(N,M,arr):
    if len(arr)==M:
        ans.append(' '.join(map(str,arr)))
        return
    for i in range(1,N+1):
        if len(arr)==0 or i >= arr[-1]:
            DFS(N,M,arr+[i])

N, M=map(int, input().split())

DFS(N,M,[])

print('\n'.join(ans))