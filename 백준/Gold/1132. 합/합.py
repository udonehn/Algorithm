def find(arr, a):
    for i in range(len(a)-1,-1,-1):
        TF=True
        for j in arr:
            if a[i][0]==j[0]:
                TF=False
        if TF:
            return i
                
N=int(input())

arr=[]
for _ in range(N):
    arr.append(list(input()))

alpha=dict()

for i in arr:
    for j in i:
        if j not in alpha:
            alpha[j]=0

for i in range(N):
    for j in range(len(arr[i])):
        n=10**(len(arr[i])-j-1)
        alpha[arr[i][j]]+=n

a = sorted(alpha.items(), key=lambda x : x[1], reverse=True)

if len(alpha)==10:
    for i in arr:
        if a[-1][0]==i[0]:
            n = find(arr,a)
            for j in range(n,len(alpha)-1):
                a[j], a[j+1] = a[j+1], a[j] 

value=dict()
num=9
for i in a:
    value[i[0]]=num
    num-=1

sum=0
for i in range(N):
    for j in range(len(arr[i])):
        sum+=10**(len(arr[i])-j-1)*value[arr[i][j]]

print(sum)