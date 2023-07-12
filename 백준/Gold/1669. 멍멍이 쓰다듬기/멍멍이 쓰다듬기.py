a, b = map(int, input().split())
count = 0
sum=0
n=1
while sum<b-a:
    sum = sum + n*2
    count += 2
    n +=1
n-=1
sum-=n
count-=1
if b-a == sum:
    pass
elif sum<b-a:
    count+=1
    
elif sum>b-a:
    count-=1
    if sum-n<b-a:
        count+=1

if b-a == 3:
    count=3

if count<0:
    count = 0
print(count)