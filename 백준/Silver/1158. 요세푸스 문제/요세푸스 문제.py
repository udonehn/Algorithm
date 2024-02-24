from collections import deque

if __name__ == "__main__":
    N, K = map(int, input().split())
    queue = deque([i for i in range(1, N+1)])
    arr = []

    while queue:
        for _ in range(K-1):
            queue.append(queue.popleft())
        arr.append(queue.popleft())

    answer = "<"+str(arr[0])
    for num in arr[1:]:
        answer += ", "
        answer += str(num)
    answer += ">"
    print(answer)
