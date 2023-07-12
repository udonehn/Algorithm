import sys
input=lambda:sys.stdin.readline().rstrip()

def solve(s, TF):
    st=0
    en=len(s)-1
    while st<en:
        if s[st]==s[en]:
            st+=1
            en-=1
        else:
            if TF==True:
                return 2
            return min(solve(s[st+1:en+1],True),solve(s[st:en],True))
    if TF==True:
        return 1
    else:
        return 0


for _ in range(int(input())):
    print(solve(list(input()),False))