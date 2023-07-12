N = int(input())
pec = 1
for i in range(1,N+1):
  pec*=i
pecto = list(str(pec))
ans=0
while True:
  if pecto.pop()=='0':
    ans+=1
  else:
    break
print(ans)