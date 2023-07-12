def preorder(tree,node):
    if node=='.':
        return
    print(node, end='')
    preorder(tree, tree[node][0])
    preorder(tree, tree[node][1])

def inorder(tree,node):
    if node=='.':
        return
    inorder(tree, tree[node][0])
    print(node, end='')
    inorder(tree, tree[node][1])
    
def postorder(tree,node):
    if node=='.':
        return
    postorder(tree, tree[node][0])
    postorder(tree, tree[node][1])
    print(node, end='')
    
N=int(input())

tree={}
for _ in range(N):
    a,b,c=input().split()
    tree[a]=[b,c]

preorder(tree,'A')
print()
inorder(tree,'A')
print()
postorder(tree,'A')