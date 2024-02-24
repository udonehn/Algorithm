import sys
from heapq import heappop, heappush
input = lambda :sys.stdin.readline()


def solve(N, K, gems, knapsack):
    result = 0
    knapsack.sort()
    gems.sort()

    heap = []
    index = 0
    for bag in knapsack:
        while index < N and gems[index][0] <= bag:
            heappush(heap, (-gems[index][1], gems[index][0]))
            index+=1
        if heap:
            value = -heappop(heap)[0]
            result+=value

    return result



if __name__=="__main__":
    N, K = map(int, input().split())
    gems = []
    for _ in range(N):
        M, V = map(int, input().split())
        gems.append((M, V))

    knapsack = []
    for _ in range(K):
        knapsack.append(int(input()))

    print(solve(N, K, gems, knapsack))

