input()
arr = list(map(int, input().split()))
max = max(arr)
a =[True for _ in range(0, max)]
a[0]=False
for i in range(0, max):
    if a[i]==True:
        for j in range(i+1,max):
            if (j+1)%(i+1)==0:
                a[j]=False
count=0
for i in arr:
    if a[i-1]==True:
        count+=1
print(count)