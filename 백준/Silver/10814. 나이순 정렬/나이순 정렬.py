N=int(input())
arr=[]
for i in range(N):
    age, name=input().split()
    age=int(age)
    arr.append([age,name,i+1])
arr.sort(key=lambda x:(x[0],x[2]))

for i in arr:
    print(i[0],i[1])