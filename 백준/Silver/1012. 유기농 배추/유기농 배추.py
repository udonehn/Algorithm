for _ in range(int(input())):
    M, N, K=map(int,input().split())
    XY=[[0 for _ in range(M)]for _ in range(N)]
    for _ in range(K):
        X,Y=map(int,input().split())
        XY[Y][X]=1
    graph=[[]for _ in range(K)]
    cnt, ind=0,0
    dic=dict()
    for i in range(N):
        for j in range(M):
            if XY[i][j]==1:
                if i>0 and XY[i-1][j]==1:
                    graph[cnt].append(ind-M)
                if j>0 and XY[i][j-1]==1:
                    graph[cnt].append(ind-1)
                if i<N-1 and XY[i+1][j]==1:
                    graph[cnt].append(ind+M)
                if j<M-1 and XY[i][j+1]==1:
                    graph[cnt].append(ind+1)
                dic[ind]=cnt
                cnt+=1
            ind+=1
    
    visited=[]
    count=0
    for i in range(len(graph)):
        if i not in visited:
            stack=[i]
            while stack:
                v=stack.pop()
                if v not in visited:
                    visited.append(v)
                    l=[dic[j]for j in graph[v]]
                    stack.extend(l)
            count+=1
            
    print(count)