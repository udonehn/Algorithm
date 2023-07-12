arr = []
A='a'
while True:
    A = input()
    if A == '0':
        break
    arr.append(A)
    
for i in arr:
    text = list(i)
    if len(text) == 1:
        print('yes')
        continue
    for j in range(int(len(text)/2)):
        if text[j]!=text[-1-j]:
            print('no')
            break
        if j == int(len(text)/2)-1:
            print('yes')