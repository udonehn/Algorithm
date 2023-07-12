for _ in range(int(input())):
    k=int(input())
    n=int(input())
    arr=[i+1 for i in range(n)]
    for _ in range(k):
        for i in range(n):
            if i==0:
                arr.append(1)
            else:
                arr.append(arr[-1]+arr[-n])
    print(arr[-1])