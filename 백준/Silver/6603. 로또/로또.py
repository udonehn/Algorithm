import sys
input = lambda : sys.stdin.readline().rstrip()

def recursion(set_length, s, l, index):
    if len(l) == 6:
        print(' '.join(list(map(str, l))))
        return
    for i in range(index, set_length):
        recursion(set_length, s, l+[s[i]], i+1)
        

def solve(k, list):
    recursion(k, list, [], 0)

if __name__=="__main__":
    while True:
        input_list = list(map(int, input().split()))
        if len(input_list)==0:
            break
        solve(input_list[0], input_list[1:])
        print()