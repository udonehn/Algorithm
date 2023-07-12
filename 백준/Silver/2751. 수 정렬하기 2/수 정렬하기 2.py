import sys
arr= []
for i in range(int(input())):
    arr.append(int(sys.stdin.readline().strip()))
for i in sorted(arr):
    print(i)