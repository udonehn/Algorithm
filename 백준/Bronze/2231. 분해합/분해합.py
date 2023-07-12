N = int(input())
j=0
while True:
    Ns=str(j)
    sum=0
    for i in list(Ns):
        sum+=int(i)
    sum+=int(Ns)
    if sum==N:
        break
    j+=1
    if j ==N:
        j=0
        break
print(j)