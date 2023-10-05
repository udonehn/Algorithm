import sys
input = lambda:sys.stdin.readline().rstrip()

def solve(n):
    n_copy=n
    s=1
    while n_copy-2**s>=0:
        n_copy-=2**s
        s+=1
    s-=1

    ans=["4" for _ in range(s+1)]

    for i in range(s,-1,-1):
        if n_copy-2**i>=0:
            n_copy-=2**i
            ans[s-i]="7"

    return "".join(ans)


if __name__ == "__main__":
    n=int(input())
    print(solve(n-1))