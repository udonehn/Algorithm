long = ''
num = int(input())

for i in range(1, num+1):
    for j in range(num-i):
        long+=' '
    for j in range(i):
        long+='*'
    long+='\n'
print(long)