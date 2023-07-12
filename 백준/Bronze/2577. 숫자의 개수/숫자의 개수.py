a=1
for i in range(3):
    a*=int(input())

num=str(a)

c=[0]*10

for i in num:
    c[int(i)]+=1

for i in range(10):
    print(c[i])