N = int(input())
def hanoi(n, A,B,C):
    if n ==1:
        print(A,C)
    else:
        hanoi(n-1,A,C,B)
        print(A,C)
        hanoi(n-1,B,A,C)


print(2**N-1)
if N<=20:
    hanoi(N,'1','2','3')