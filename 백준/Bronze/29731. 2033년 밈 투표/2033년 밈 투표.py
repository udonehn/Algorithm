arr = ["Never gonna give you up",
"Never gonna let you down",
"Never gonna run around and desert you",
"Never gonna make you cry",
"Never gonna say goodbye",
"Never gonna tell a lie and hurt you",
"Never gonna stop"]

arr2=[]
for _ in range(int(input())):
    arr2.append(input())

def check(arr2):
    for i in arr2:
        if i not in arr:
            return True
    return False

if check(arr2):
    print("Yes")
else:
    print("No")