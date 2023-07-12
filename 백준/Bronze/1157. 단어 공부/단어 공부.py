a = [0 for i in range(26)]

s = input().upper()
for i in list(s):
    a[ord(i)-65]+=1

max=0
TF = False

for i in range(26):
    if a[max]<a[i]:
        max=i
        TF = False
    elif a[max]==a[i] and i!=0:
        TF = True

if(TF==True):
    print("?")
else:
    print(chr(max+65))