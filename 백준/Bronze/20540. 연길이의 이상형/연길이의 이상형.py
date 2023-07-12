A=['E','S','T','J']
B=['I','N','F','P']

mbti=input()
for i in range(len(mbti)):
    if mbti[i] in A:
        print(B[i],end='')
    else:
        print(A[i],end='')