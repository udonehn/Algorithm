arr=[]
for _ in range(2):
    arr.append(list(map(int, input().split())))
for i in arr:
    print(i[0]*6+i[1]*3+i[2]*2+i[3]+i[4]*2)