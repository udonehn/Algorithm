arr=list(input())
bomb=list(input())

stack=[]
stack2=[]
count=0
for i in arr:
    stack.append(i)
    
    if i == bomb[count]:
        count+=1
    elif i == bomb[0]:
        stack2.append(count)
        count=1
    else:
        stack2=[]
        count=0
    
    if count==len(bomb):
        for _ in range(len(bomb)):
            stack.pop()
        if len(stack2)!=0:
            count=stack2.pop()
        else:
            count=0

if len(stack)!=0:
    print(''.join(stack))
else:
    print('FRULA')