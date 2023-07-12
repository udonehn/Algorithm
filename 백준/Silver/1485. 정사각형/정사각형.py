import sys
input=lambda:sys.stdin.readline().rstrip()

for _ in range(int(input())):
    arr=[]
    for _ in range(4):
        arr.append(list(map(int, input().split())))
    arr.sort()
    zero_one = (arr[0][0]-arr[1][0])**2+(arr[0][1]-arr[1][1])**2
    zero_two = (arr[0][0]-arr[2][0])**2+(arr[0][1]-arr[2][1])**2
    one_three = (arr[1][0]-arr[3][0])**2+(arr[1][1]-arr[3][1])**2
    two_three = (arr[2][0]-arr[3][0])**2+(arr[2][1]-arr[3][1])**2

    zero_three = (arr[0][0]-arr[3][0])**2+(arr[0][1]-arr[3][1])**2
    one_two = (arr[1][0]-arr[2][0])**2+(arr[1][1]-arr[2][1])**2

    if (zero_one == zero_two == one_three == two_three) and (zero_three == one_two):
        print(1)
    else:
        print(0)