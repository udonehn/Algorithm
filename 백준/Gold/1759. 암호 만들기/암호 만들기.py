import sys
input = lambda:sys.stdin.readline().rstrip()

v_set=set(['a','i','u','e','o'])

def check(pw):
    v=0
    c=0
    for i in list(pw):
        if i in v_set:
            v+=1
        else:
            c+=1
    if v>=1 and c>=2:
        return True
    else:
        return False

def solve(L, C, alphabet, pw, index):
    if len(pw)==L:
        if check(pw):
            print(pw)
    
    for i in range(index, C):
        solve(L, C, alphabet, pw+alphabet[i], i+1)

if __name__=="__main__":
    L, C = map(int, input().split())
    alphabet=input().split()
    solve(L, C, sorted(alphabet), '', 0)