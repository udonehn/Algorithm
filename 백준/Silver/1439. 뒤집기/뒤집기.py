import sys
import math
input=lambda:sys.stdin.readline().rstrip()

S=list(input())
p=S[0]
count=0
for i in S:
    if i!=p:
        p=i
        count+=1
        
print(math.ceil(count/2))