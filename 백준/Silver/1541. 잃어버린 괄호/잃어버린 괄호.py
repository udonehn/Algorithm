n = input()
arr=[]
for i in n.split('+'):
    for j in i.split('-'):
        arr.append(j)
        arr.append('-')
    arr.pop()
    arr.append('+')
arr.pop()
TF=False

for i in range(len(arr)):
    if arr[i] == '-':
        TF=True
    elif arr[i] =='+' and TF==True:
        arr[i] = '-'
    elif arr[i] !='-' and arr[i] !='+':
        arr[i] = int(arr[i])

result=arr[0]
if len(arr)!=1:
    op=arr[1]
    for i in range(1,len(arr)):
        if arr[i] == '+':
            op='+'
        elif arr[i]== '-':
            op='-'
        else:
            if op=='+':
                result+=arr[i]
            elif op=='-':
                result-=arr[i]
print(result)
