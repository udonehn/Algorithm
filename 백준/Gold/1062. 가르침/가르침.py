from itertools import combinations
import sys

input=lambda:sys.stdin.readline().rstrip()

N, K = map(int, input().split())

word=[]
for _ in range(N):
    word.append(list(input().lstrip('anta').rstrip('tica')))

if K<5:
    print(0)
else:
    antic=set(['a','n','t','i','c'])

    alpha=set()
    for i in word:
        alpha.update(i)
    alpha=alpha-antic

    if len(alpha)<K-5:
        print(N)
    else:
        al = list(combinations(alpha,K-5))
        
        m=0
        for i in al:
            count=0
            w=antic|set(i)
            for j in word:
                cnt=0
                for k in j:
                    if k in w:
                        cnt+=1
                if cnt==len(j):
                    count+=1
            m=max(m,count)
            
        print(m)