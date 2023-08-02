from collections import deque
import sys
input=lambda:sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())

height=1
while 2**height<N:
    height+=1

tree = [0]*(2**(height+1))

for i in range(N):
    tree[2**height+i]=int(input())

c=2**height-1
while c>0:
    tree[c]=tree[c*2]+tree[c*2+1]
    c-=1


def update(b,c):
    p=2**height-1+b
    difference = c - tree[p]
    while True:
        tree[p] = tree[p] + difference
        if p==1:
            break
        p=p//2


def ans(b,c):
    start, end = 2**height-1+b, 2**height-1+c
    result = 0
    while start<end:
        if start%2==1:
            result+=tree[start]
        start=(start+1)//2

        if end%2==0:
            result+=tree[end]
        end=(end-1)//2
        
    if start==end:
        result+=tree[start]
    print(result)


m=k=0
while m<M or k<K:
    a,b,c=map(int, input().split())

    if a==1:
        update(b,c)
        m+=1
    elif a==2:
        ans(b,c)
        k+=1
