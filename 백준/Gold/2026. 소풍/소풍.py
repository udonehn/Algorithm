import sys
input = lambda :sys.stdin.readline().rstrip()


def check(graph, answer, candidate):
    for answer_element in answer:
        if candidate not in graph[answer_element]:
            return False
    return True
    

def solve(K, N, start, graph, answer):
    if len(answer)==K:
        for i in answer:
            print(i)
        sys.exit(0)
        
    for i in range(start, N+1):
        if len(graph[i])>=K-1:
            if check(graph, answer, i):
                solve(K, N, i+1, graph, answer+[i])


if __name__=="__main__":
    K, N, F = map(int, input().split())
    student=dict()
    for i in range(1, N+1):
        student[i]=[]

    for _ in range(F):
        a,b=map(int, input().split())
        student[a].append(b)
        student[b].append(a)

    solve(K, N, 1, student, [])
    print(-1)