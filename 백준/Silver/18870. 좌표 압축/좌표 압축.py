input()
arr = list(map(int, input().split()))
arr_sort=sorted(arr)
dic=dict()
cnt=0
for i in arr_sort:
    if i not in dic:
        dic[i]=cnt
        cnt+=1
for i in arr:
    print(dic[i], end=' ')