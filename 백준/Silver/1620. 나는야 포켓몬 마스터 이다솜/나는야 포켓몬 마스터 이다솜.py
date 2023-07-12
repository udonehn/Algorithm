import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
dic = dict()
for i in range(N):
    dic[i+1]=sys.stdin.readline().rstrip()
reversed_dict=dict(map(reversed,dic.items()))

for _ in range(M):
    ans = sys.stdin.readline().rstrip()
    try:
        ans=int(ans)
        print(dic[ans])
    except:
        print(reversed_dict[ans])