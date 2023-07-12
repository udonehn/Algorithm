def test(arr, P):
    for i in range(len(P)):
        if arr[i] != P[i]:
            return False
    return True

N = int(input())
M = int(input())
S = list(input())

P = 'IO'
for _ in range(N-1):
    P+='IO'
P+='I'
count=0
i=0
TF=False

while True:
    if S[i]=='I':
        TF = test(S[i:i+N*2+1], P)
        if TF:
            count+=1
    i+=1
    if i>M-N*2-1:
        break
print(count)