num = int(input())
OX = []
scores = [0] * num
for i in range(num):
    OX.append(input())

for i in range(num):
    score=0
    for j in list(OX[i]):
        if j == 'O':
            score+=1
            scores[i]+=score
        else:
            score=0

for i in range(num):
    print(scores[i])