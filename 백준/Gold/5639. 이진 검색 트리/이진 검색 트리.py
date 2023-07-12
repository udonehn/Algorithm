import sys
sys.setrecursionlimit(10 ** 6)
def postorder(tree, root):
    if root==None:
        return
    postorder(tree,tree[root][0])
    postorder(tree,tree[root][1])
    print(root)

def insert(tree, root, N):
    while root is not None:
        if root>N:
            i=0
        else:
            i=1
        p=root
        root=tree[root][i]
    tree[p][i]=N
    tree[N]=[None, None]

tree={}
root=int(input())
tree[root]=[None, None]
while True:
    try:
        insert(tree, root, int(input()))
    except:
        break
postorder(tree,root)