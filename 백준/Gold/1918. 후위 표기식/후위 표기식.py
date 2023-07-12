s = list(input())
stack = []
ans=''
for i in s:
  if i == '+' or i=='-':
    while True:
      if len(stack) == 0:
        break
      if stack[-1]!='(':
        p=stack.pop()
        ans+=p
      elif stack[-1]=='(':
        break
    stack.append(i)
        
  elif i == '*' or i=='/':
    while True:
      if len(stack) == 0:
        break
      if stack[-1]=='*'or stack[-1]=='/':
        p=stack.pop()
        ans+=p
      elif stack[-1]=='+' or stack[-1]=='-' or stack[-1]=='(':
        break
    stack.append(i)
  elif i == '(':
    stack.append(i)
  elif i == ')':
    while True:
      if stack[-1]!='(':
        p=stack.pop()
        ans+=p
      elif stack[-1]=='(':
        stack.pop()
        break
  else:
    ans+=i

while len(stack)!=0:
  ans+=stack.pop()
  
print(ans)