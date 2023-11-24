X = int(input())
total=0
for _ in range(int(input())):
    total+=(lambda l:l[0]*l[1])(list(map(int,input().split())))
if X == total:
    print("Yes")
else:
    print("No")