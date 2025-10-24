def hanoi(answer, n, dep, lay, arr):
    if n == 1:
        answer.append([dep, arr])
        return
    hanoi(answer, n-1, dep, arr, lay)
    answer.append([dep, arr])
    hanoi(answer, n-1, lay, dep, arr)

def solution(n):
    answer = []
    hanoi(answer, n, 1, 2, 3)
    return answer