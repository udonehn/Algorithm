ans=[]

def DFS(N,M,arr,Ns):
    if len(arr)==M:
        ans.append(' '.join(map(str,arr)))
        return
    for i in Ns:
        if i not in arr:
            DFS(N,M,arr+[i],Ns)

N, M=map(int, input().split())
Ns=list(map(int,input().split()))

DFS(N,M,[],sorted(Ns))

print('\n'.join(ans))