import sys
input = lambda:sys.stdin.readline().rstrip()
stack=[]
for _ in range(int(input())):
    i=input().split()
    if i[0]=='push':
        stack.append(i[1])
    elif i[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif i[0]=='size':
        print(len(stack))
    elif i[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif i[0]=='top':
        if len(stack)==0:
            print(-1)
        else:
            N=stack.pop()
            print(N)
            stack.append(N)