import sys

tree=dict()
while True:
    t=sys.stdin.readline().rstrip()
    if not t:
        break
    if t in tree:
        tree[t]+=1
    else:
        tree[t]=1
sum=0
for i in tree.values():
    sum+=i
trees=sorted(tree.keys())

for i in trees:
    percent = (tree[i]/sum)*100
    print(i, end=' ')
    print("{:.4f}".format(percent))