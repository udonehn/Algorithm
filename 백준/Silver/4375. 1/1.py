N = []
while True:
    try:
        N.append(int(input()))
    except:
        break
for i in N:
    if i%2==0 or list(str(i))[-1] == '5':
        print(-1)
    else:
        Is=''
        while True:
            Is+='1'
            if int(Is)%i==0:
                break
        print(len(str(Is)))