import sys
input = lambda:sys.stdin.readline().rstrip()


if __name__ == "__main__":
    A = input()
    B = input()
    C = input()
    print(int(A)+int(B)-int(C))
    print(int(A+B)-int(C))

