from collections import deque
T= int(input())
for _ in range(T):
    command=list(input())
    le = int(input())
    TF=True
    deq=deque(input().lstrip('[').rstrip(']').split(','))

    for i in command:

        if i=='R':
            TF=not TF
        else:
            if len(deq)==0 or deq[0]=='':
                TF='error'
                break
            if TF==True:
                deq.popleft()
            else:
                deq.pop()
    p=[]
    if TF=='error':
        print('error')
    else:
        if TF==False:
            deq.reverse()
        for i in deq:
                p.append(i)
        print('['+','.join(p)+']')