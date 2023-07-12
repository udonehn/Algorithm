import sys

N = int(sys.stdin.readline())
arr = set()

for i in range(N):
    arr.add(sys.stdin.readline())
arr = list(arr)

# for i in range(len(arr)):
#     for j in range(len(arr)-i-1):
#         if(len(arr[j])>len(arr[j+1])):
#             arr[j], arr[j+1] = arr[j+1], arr[j]

arr.sort(key=len)

leng = len(arr[0])
arrs=[]
start=0
end=0
# print(arr)
for i in range(len(arr)):
    if len(arr[i])>leng:
        arrs.extend(sorted(arr[start:end]))
        leng = len(arr[i])
        start = i
        end = i+1
    else:
        end+=1
        
arrs.extend(sorted(arr[start:]))

for i in arrs:
    print(i,end='')
# print(arrs)