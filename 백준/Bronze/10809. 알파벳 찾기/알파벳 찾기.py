A = [-1]*26

s = list(input())

for i in range(len(s)):
    if A[ord(s[i])-97] == -1:
        A[ord(s[i])-97] = i
        
for i in A:
    print(i, end=' ')