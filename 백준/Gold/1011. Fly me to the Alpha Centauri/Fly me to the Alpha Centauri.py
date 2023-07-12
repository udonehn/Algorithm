for _ in range(int(input())):
    a,b=map(int, input().split())
    d = b-a
    i=1
    sum=0
    while sum<d:
        sum+=i*2
        i+=1
    i-=1
    
    if sum==i:
        print(i*2)
    elif sum-i==d:
        print(i*2-1)
    elif sum-i<d:
        print(i*2)
    elif sum-i*2==d:
        print(i*2-2)
    elif sum-i*2<d:
        print(i*2-1)