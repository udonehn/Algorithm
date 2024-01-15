def solve(N, arr):
    if N < 3:
        return 0
    arr.sort()
    count=0
    for i in range(N):
        left = 0
        right = N-1
        while left<right:
            if arr[left] + arr[right] == arr[i]:
                if left == i:
                    left+=1
                elif right == i:
                    right-=1
                else:
                    count += 1
                    break
            elif arr[left] + arr[right] > arr[i]:
                right -= 1
            elif arr[left] + arr[right] < arr[i]:
                left += 1

    return count

if __name__=="__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    print(solve(N, arr))