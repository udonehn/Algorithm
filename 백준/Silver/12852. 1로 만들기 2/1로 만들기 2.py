N = int(input())
arr = [-1,0,1,1]
arr2=[-1,[],[1],[1]]
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
    m=min([minus,three,two])
    
    if m==minus:
        arr2.append(arr2[i-1]+[i-1])
    elif m==three:
        arr2.append(arr2[int(i/3)]+[int(i/3)])
    elif m==two:
        arr2.append(arr2[int(i/2)]+[int(i/2)])
    
    arr.append(m+1)
    i+=1
print(arr[N])

arr2[N].reverse()
print(N,end=' ')
for i in arr2[N]:
    print(i,end=' ')