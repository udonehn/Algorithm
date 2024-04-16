import sys
input = lambda: sys.stdin.readline().rstrip()


if __name__ == "__main__":
    s = set()
    string = list(input())
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            s.add(''.join(string[i:j]))
    print(len(s))
