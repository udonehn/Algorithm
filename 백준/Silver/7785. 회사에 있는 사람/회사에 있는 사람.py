s=set()
for _ in range(int(input())):
    name, status = input().split()
    if status == "enter":
        s.add(name)
    else:
        s.remove(name)

l = list(s)
l.sort()
l.reverse()
for n in l:
    print(n)