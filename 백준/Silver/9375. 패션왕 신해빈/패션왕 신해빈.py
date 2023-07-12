N = int(input())
for _ in range(N):
    a = int(input())
    dic=dict()
    for _ in range(a):
        c = input().split()[1]
        if c in dic:
            dic[c]+=1
        else:
            dic[c]=1
    if len(dic)==1:
        print(dic[c])
    else:
        sum=1
        for i in dic.values():
            sum*=(i+1)
        print(sum-1)