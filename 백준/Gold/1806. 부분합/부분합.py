import sys
input = lambda:sys.stdin.readline().rstrip()

def solve(arr, N, S):
    if S==0:
        return 1
    answer=N+1
    left_index=0
    while True:
        right_index = left_index
        count=0
        sum=0

        while sum<S and right_index<N:
            sum+=arr[right_index]
            right_index+=1
            count+=1

        if sum<S and right_index==N:
            break

        while sum>=S:
            sum-=arr[left_index]
            left_index+=1
            count-=1

        answer=min(count+1, answer)
        if answer == 1:
            break

    if answer == N + 1:
        return 0
    else:
        return answer


if __name__=="__main__":
    N, S = map(int, input().split())
    arr = list(map(int,input().split()))


    print(solve(arr, N, S))
