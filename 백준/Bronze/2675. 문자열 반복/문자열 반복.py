a = int(input())
s = ''

for i in range(a):
    q, w = input().split(' ')
    for j in list(w):
        s+=j*int(q)
    s+='\n'

print(s)