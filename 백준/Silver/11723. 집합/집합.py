import sys
N = int(sys.stdin.readline())
s = set()
arr = []
for i in range(20):
    arr.append(i+1)
for _ in range(N):
  co = sys.stdin.readline().strip().split()
  if len(co)==2:
      co[1]=int(co[1])
  if co[0] == 'add':
    s.add(co[1])
  elif co[0] == 'remove':
    s.discard(co[1])
  elif co[0] == 'check':
    if co[1] in s:
      print(1)
    else:
      print(0)
  elif co[0] == 'toggle':
    if co[1] in s:
      s.remove(co[1])
    else:
      s.add(co[1])
  elif co[0] == 'all':
    s = set(arr)
  elif co[0] == 'empty':
    s.clear()