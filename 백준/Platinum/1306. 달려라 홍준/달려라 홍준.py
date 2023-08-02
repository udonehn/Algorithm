import sys
input=lambda:sys.stdin.readline().rstrip()

def init(k, M, ad):
    tree = [0]*(2**(k+1))
    for i in range(M*2-2):
        tree[2**k+i] = ad[i]
    i = 2**k-1
    while i>0:
        tree[i]=max(tree[i*2],tree[i*2+1])
        i-=1
    return tree

def update(node, i):
    tree[node] = i
    while node!=1:
        node//=2
        tree[node] = max(tree[node*2], tree[node*2+1])

if __name__ == "__main__":
    N, M = map(int, input().split())
    ad = list(map(int, input().split()))
    k = 1
    while 2**k<M*2-1:
        k+=1

    tree = init(k, M, ad)

    ans=[]
    cursor = M*2-2
    for i in ad[M*2-2:]:
        update(cursor+2**k, i)
        ans.append(str(tree[1]))
        cursor+=1
        cursor = cursor%(M*2-1)
    
    print(' '.join(ans))