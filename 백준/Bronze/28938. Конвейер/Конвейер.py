answer = 0
input()
for num in map(int, input().split()):
    answer += num
if answer > 0:
    print("Right")
elif answer < 0:
    print("Left")
else:
    print("Stay")