N=int(input())

arr=list(map(int, input().split()))

maximum=[i for i in arr]
minimum=[i for i in arr]


for _ in range(N-1):
    arr=list(map(int, input().split()))
    tmp_max=[]
    tmp_min=[]
    for j in range(3):
        m=[]
        if j==0:
            m.append(maximum[0]+arr[0])
            m.append(maximum[1]+arr[0])
            
            m.append(minimum[0]+arr[0])
            m.append(minimum[1]+arr[0])
            
        elif j==1:
            m.append(maximum[0]+arr[1])
            m.append(maximum[1]+arr[1])
            m.append(maximum[2]+arr[1])
            
            m.append(minimum[0]+arr[1])
            m.append(minimum[1]+arr[1])
            m.append(minimum[2]+arr[1])
            
        elif j==2:
            m.append(maximum[1]+arr[2])
            m.append(maximum[2]+arr[2])
            
            m.append(minimum[1]+arr[2])
            m.append(minimum[2]+arr[2])
            
        tmp_max.append(max(m))
        tmp_min.append(min(m))
    maximum=[i for i in tmp_max]
    minimum=[i for i in tmp_min]
print(max(maximum),end=' ')
print(min(minimum),end=' ')