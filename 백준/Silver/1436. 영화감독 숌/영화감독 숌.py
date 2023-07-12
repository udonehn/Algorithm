n = int(input())
num = 0
count = 0
cnt = 0
while True:
    l = list(str(num))
    for i in l:
        if i == '6':
            count +=1
        else:
            count = 0
        if count == 3:
            cnt+=1
            break
    count = 0
    if n==cnt:
        print(num)
        break
    num+=1