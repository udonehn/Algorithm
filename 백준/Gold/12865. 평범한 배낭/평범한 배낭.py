import sys
input = lambda :sys.stdin.readline()

def solve(N,K,items,dp):
    for i in range(1,N+1):
        for j in range(1,K+1):
            weight, value = items[i-1]
            if weight>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j], dp[i-1][j-weight]+value)
    return dp[N][K]


if __name__=="__main__":
    N, K = map(int, input().split())
    items=[]
    for _ in range(N):
        W, V = map(int, input().split())
        items.append((W, V))
    dp=[[0 for j in range(K+1)] for i in range(N+1)]

    print(solve(N,K,items,dp))

