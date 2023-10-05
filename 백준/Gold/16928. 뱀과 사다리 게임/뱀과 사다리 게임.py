import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def BFS(graph):
    visited = [False for _ in range(101)]
    visited[1] = True
    queue = deque()
    if 1 in graph:  #뱀 또는 사다리가 있을 때
        queue.append((graph[1], 0))  
    else:
        queue.append((1,0)) #좌표, 답

    while queue:
        square, ans = queue.popleft()
        for i in range(1,7):
            if i+square > 100:
                continue
            if i+square == 100:
                return ans+1
            if i+square in graph:   #뱀 또는 사다리가 있을 때
                if not visited[i+square]:
                    queue.append((graph[i+square], ans+1))
            else:
                if not visited[i+square]:
                    queue.append((i+square,ans+1))
            visited[i+square]=True


if __name__ == "__main__":
    ladder, snake = map(int, input().split())
    graph = dict()

    for _ in range(ladder+snake):
        A, B = map(int, input().split())
        graph[A]=B

    print(BFS(graph))