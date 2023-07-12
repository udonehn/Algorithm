from collections import deque

N = int(input())
deq = deque(list(input()))
deq2 = deque()
dic = {}

for i in range(N):
    dic[chr(65+i)] = int(input())
    
while deq:
    m = deq.popleft()
    if m!='+' and m!='-' and m!='*' and m!='/':
        deq2.append(dic[m])
    else:
        y = deq2.pop()
        x = deq2.pop()
        if m=='+':
            deq2.append(x+y)
        elif m=='-':
            deq2.append(x-y)
        elif m=='*':
            deq2.append(x*y)
        elif m=='/':
            deq2.append(x/y)
            
print(format(deq2[0],'.2f'))