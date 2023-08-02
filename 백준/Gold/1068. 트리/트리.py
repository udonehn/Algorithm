from collections import deque
import sys
input=lambda:sys.stdin.readline().rstrip()

N = int(input())
node = list(map(int, input().split()))
tree = [[] for _ in range(N)]
visited=[False]*N

for i in range(N):
    if node[i] == -1:
        root = i
    else:
        tree[i].append(node[i])
        tree[node[i]].append(i)

deleted = int(input())

def DFS(number):
    visited[number] = True
    stack = [number]
    ans=0
    while stack:
        n = stack.pop()
        cnt=0
        for i in tree[n]:
            if not visited[i] and i != deleted:
                visited[n] = True
                stack.append(i)
                cnt+=1
        if cnt==0:
            ans+=1
    return ans

if deleted == root:
    print(0)
else:
    print(DFS(root))