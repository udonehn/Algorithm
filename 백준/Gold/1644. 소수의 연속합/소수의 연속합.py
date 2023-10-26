if __name__=="__main__":
    N=int(input())
    
    # 에라토스테네스의 체
    arr=[True for _ in range(N+1)]
    for i in range(2, N+1):
        if arr[i]:
            for j in range(i*2, N+1, i):
                arr[j]=False

    # 누적합
    prefix=[0]
    tmp=0
    for i in range(2, N+1):
        if arr[i]:
            tmp+=i
            prefix.append(tmp)

    # 정답 카운트
    prefix.reverse()
    ans=0
    for i in range(len(prefix)):
        if prefix[i]<N:
            break
        for j in range(i+1, len(prefix)):
            if prefix[i]-prefix[j]==N:
                ans+=1
            if prefix[i]-prefix[j]>N:
                break
                
    print(ans)