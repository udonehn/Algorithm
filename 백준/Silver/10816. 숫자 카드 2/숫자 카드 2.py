input()
arr=input().split()
dic=dict()
for i in arr:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
input()
ans=input().split()
for i in ans:
    if i in dic:
        print(dic[i],end=' ')
    else:
        print(0,end=' ')