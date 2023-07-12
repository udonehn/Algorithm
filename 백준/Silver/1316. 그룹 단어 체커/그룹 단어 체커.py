import sys
input=lambda:sys.stdin.readline().rstrip()

def check(word):
    s=set()
    c=word[0]
    s.add(c)
    for i in word[1:]:
        if i !=c:
            if i in s:
                return False
            else:
                s.add(i)
                c=i
    return True


cnt=0
for _ in range(int(input())):
    if check(input()):
        cnt+=1
print(cnt)