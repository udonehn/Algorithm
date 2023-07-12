from collections import deque
arr=[]
for _ in range(int(input())):
    arr.append(input())
stack=deque()
for i in arr:
    p=''
    stack.clear()
    for j in list(i):
        if j == '(':
            stack.append('(')
        elif j == ')':
            if len(stack) == 0:
                p+='NO'
                break
            if stack.pop() == '(':
                pass
            else:
                p+='NO'
                break
    if len(stack) == 0 and p == '':
        print('YES')
    else:
        print('NO')