N = int(input())
odd=0
even=0
for i in list(map(int, input().split())):
    if i%2==0:
        even+=1
    else:
        odd+=1
if even>odd:
    print("Happy")
else:
    print("Sad")