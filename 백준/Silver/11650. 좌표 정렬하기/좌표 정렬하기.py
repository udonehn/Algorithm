import sys
arr=[]
for _ in range(int(sys.stdin.readline().strip())):
    arr.append([int(i) for i in sys.stdin.readline().strip().split()])
arr.sort()
for i in arr:
    for j in i:
        print(str(j)+' ',end='')
    print()