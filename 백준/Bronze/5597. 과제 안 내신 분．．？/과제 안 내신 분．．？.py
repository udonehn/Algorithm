arr = [False] * 30

for i in range(28):
    arr[int(input()) - 1] = True

for i in range(30):
    if arr[i] == False:
        print(i + 1)
