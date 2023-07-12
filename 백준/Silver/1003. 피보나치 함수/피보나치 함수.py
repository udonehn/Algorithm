T = int(input())
arr=[int(input()) for _ in range(T)]

z = [1, 0]
o = [0, 1]
max = max(arr)
if max>1:
    for i in range(2, max+1):
        z.append(z[-1]+z[-2])
        o.append(o[-1]+o[-2])
for i in arr:
    if i==0:
        print('1 0')
    elif i==1:
        print('0 1')
    else:
        print(z[i],o[i])