text=[]
while True:
    text.append(input())
    if text[-1] == '.':
        break
del text[-1]

for tex in text:
    stack = ['']
    p='yes'
    for te in tex:
        if te =='(' or te=='[':
            stack.append(te)
        if te == ')':
            if stack[-1] =='(':
                del stack[-1]
            else:
                p='no'
                break
        if te ==']':
            if stack[-1] =='[':
                del stack[-1]
            else:
                p='no'
                break
    if stack[-1] == '[' or stack[-1]== '(':
        p='no'
    print(p)