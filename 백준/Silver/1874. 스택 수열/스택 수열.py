n = int(input())
arr = []
stack = [-1]
j=0
ans=''
for _ in range(n):
    arr.append(int(input()))
for i in arr:
    if i>stack[-1]:
        while i != stack[-1]:
            j+=1
            stack.append(j)
            ans+='+'
        stack.pop()
        ans+='-'
    elif i==stack[-1]:
        stack.pop()
        ans+='-'
    else:
        break
    
if len(stack)==1:
    for i in list(ans):
        print(i)
else:
    print('NO')