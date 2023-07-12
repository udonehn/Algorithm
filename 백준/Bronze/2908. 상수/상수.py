A, B = map(list, input().split())
AA=''
BB=''

for i in range(3):
    AA+=A[-1-i]
    BB+=B[-1-i]

if(int(AA)>int(BB)):
    print(AA)
else:
    print(BB)