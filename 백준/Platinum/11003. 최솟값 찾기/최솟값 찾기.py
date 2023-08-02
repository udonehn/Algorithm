import sys
input=lambda:sys.stdin.readline().rstrip()

def update(tree, data, node):
    tree[node] = data
    while node != 1:
        node //= 2
        tree[node] = min(tree[node*2], tree[node*2+1])

if __name__ == "__main__":
    N, L = map(int, input().split())
    arr=list(map(int, input().split()))

    k=1
    while 2**k<L:
        k+=1
    
    tree = [max(arr)] * (2**(k+1))

    ans=[]
    cursor=0
    for data in arr:
        update(tree, data, cursor+2**k)
        ans.append(str(tree[1]))
        cursor+=1
        cursor = cursor%L

    print(' '.join(ans))