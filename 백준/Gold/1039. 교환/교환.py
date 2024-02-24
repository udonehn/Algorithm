import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()


def is_possible(arr):
    if len(arr) == 1:
        return False
    count = 0
    for n in arr:
        if n == '0':
            count += 1
    if len(arr) == 2 and count == 1:
        return False
    return True

def solve(arr, K):
    if not is_possible(arr):
        return -1

    queue = deque()
    candidate = []
    queue.append((arr, 0))
    visited = set()
    while queue:
        arr, count = queue.popleft()
        if count == K:
            candidate.append(''.join(arr))
            continue

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                temp = arr[:]
                if temp[j] == '0' and i == 0:
                    continue
                temp[i], temp[j] = temp[j], temp[i]
                if (''.join(temp), count + 1) in visited:
                    continue
                queue.append((temp, count + 1))
                visited.add((''.join(temp), count + 1))
    return max(list(map(int, candidate)))



if __name__ == "__main__":
    N, K = map(int, input().split())
    arr = list(str(N))
    print(solve(arr, K))