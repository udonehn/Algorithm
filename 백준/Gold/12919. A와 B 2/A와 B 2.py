import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()

def solve(S,T):
    queue=deque([T])
    while queue:
        string = queue.popleft()
        if len(string)==len(S):
            if string==S:
                return 1
            else:
                continue

        if string[-1]=='A':
            queue.append((string[:-1]))
        if string[0]=='B':
            queue.append((list(reversed(string[1:]))))

    return 0

if __name__=="__main__":
    S=list(input())
    T=list(input())
    print(solve(S,T))