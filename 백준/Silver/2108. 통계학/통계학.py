import sys

num=[]
for _ in range(int(sys.stdin.readline())):
    num.append(int(sys.stdin.readline()))

sum=0
for i in num:
    sum+=i
print(round(sum/len(num)))
num.sort()

print(num[int(len(num)/2)])

dic = dict()
for n in num:
    try:
        dic[n]+=1
    except:
        dic[n]=1
        
mod = 0
mods = []

for i in dic:
    if dic[i] > mod:
        mods.clear()
        mods.append(i)
        mod = dic[i]
    elif dic[i] == mod:
        mods.append(i)

if len(mods) == 1:
    print(mods[0])
else:
    mods.sort()
    print(mods[1])
    
print(num[-1]-num[0])