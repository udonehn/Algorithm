import sys
input = lambda :sys.stdin.readline()

if __name__=="__main__":
    N = int(input())
    arr=list(map(int ,input().split()))
    answer = [0 for _ in range(N)]
    stack=[]
    while arr:
        if not stack:
            stack.append((arr.pop(), len(arr)))
        elif stack[-1][0]>arr[-1]:
            stack.append((arr.pop(), len(arr)))
        else:
            while stack and stack[-1][0]<arr[-1]:
                _, index = stack.pop()
                answer[index] = len(arr)

    for i in answer:
        print(i, end=' ')
