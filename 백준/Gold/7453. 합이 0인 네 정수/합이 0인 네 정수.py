import sys
input = lambda:sys.stdin.readline().rstrip()

if __name__=="__main__":
    n=int(input())
    A, B, C, D = [], [], [], []
    for _ in range(n):
        a,b,c,d=map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)

    dic=dict()
    for i in range(n):
        for j in range(n):
            tmp = A[i]+B[j]
            if tmp in dic:
                dic[tmp]+=1
            else:
                dic[tmp]=1

    count = 0
    for i in range(n):
        for j in range(n):
            tmp = C[i]+D[j]
            if -tmp in dic:
                count+=dic[-tmp]

    print(count)
