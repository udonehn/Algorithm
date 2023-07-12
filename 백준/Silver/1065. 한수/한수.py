N = int(input())
count=0
for i in range(1, N+1):
    if len(str(i))<=2:
        count+=1
    else:
        l=list(str(i))
        cnt=0
        for j in range(len(l)-2):
            if int(l[j+1])-int(l[j])==int(l[j+2])-int(l[j+1]):
                cnt+=1
            if cnt==len(l)-2:
                count+=1
print(count)