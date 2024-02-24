if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    length= [0, ]
    for i in range(1, N):
        max_length = -1
        for j in range(i):
            if arr[i] > arr[j]:
                max_length = max(max_length, length[j])
        length.append(max_length+1)
    print(max(length)+1)