import sys
sys.setrecursionlimit(100000)

def get_child(a, b, node, index, l, tree):
    height = node[index][2]
    for i in range(index + 1, l):
        n, x, y = node[i]
        if y < height and a < x < b:
            left = get_child(x, b, node, i, l, tree)
            right = get_child(a, x, node, i, l, tree)
            tree[n] = [right, left]
            return n
    return -1
            

def get_tree(node, l):
    tree = dict()
    left = get_child(node[0][1], sys.maxsize, node, 0, l, tree)
    right = get_child(-sys.maxsize, node[0][1], node, 0, l, tree)
    tree[node[0][0]] = [right, left]
    return tree


def preorder(tree, root):
    stack = [root]
    order = []
    while stack:
        node = stack.pop()
        order.append(node)
        left, right = tree[node]
        if right != -1:
            stack.append(right)
        if left != -1:
            stack.append(left)

    return order

    
def postorder(tree, node, order):
    left, right = tree[node]
    if left != -1:
        postorder(tree, left, order)
    if right != -1:
        postorder(tree, right, order)
    order.append(node)
    return order
    
    
def solution(nodeinfo):
    answer = []
    l = len(nodeinfo)
    
    new_nodeinfo = []
    for i in range(l):
        new_nodeinfo.append([i + 1, nodeinfo[i][0], nodeinfo[i][1]])
        
    sorted_node = sorted(new_nodeinfo, key=lambda x: (-x[2], x[1]))
    
    tree = get_tree(sorted_node, l)

    answer.append(preorder(tree, sorted_node[0][0]))
    answer.append(postorder(tree, sorted_node[0][0], []))
    return answer