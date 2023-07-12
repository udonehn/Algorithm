ans=[]

def DFS(N,M,arr,Ns,v):
    if len(arr)==M:
        a=' '.join(map(str,arr))
        if a not in ans:
            ans.append(a)
        return
    for i in range(N):
        if i not in v:
            DFS(N,M,arr+[Ns[i]],Ns,v+[i])

N, M=map(int, input().split())
Ns=list(map(int,input().split()))

DFS(N,M,[],sorted(list(Ns)),[])

print('\n'.join(ans))