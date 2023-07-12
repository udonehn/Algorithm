N = int(input())
arr = [-1,0,1,1]
i=4
while i<=N:
    minus = arr[i-1]
    if i%3==0:
        three = arr[int(i/3)]
    else: 
        three = i*i
    if i%2==0:
        two = arr[int(i/2)]
    else:
        two = i*i
    arr.append(min([minus,three,two])+1)
    i+=1
print(arr[N])