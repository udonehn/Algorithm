ans=[]

def DFS(N,arr):
    if len(arr)==N:
        ans.append(' '.join(list(map(str,arr))))
    for i in range(1,N+1):
        if i not in arr:
            DFS(N,arr+[i])

N=int(input())

DFS(N,[])

print('\n'.join(ans))