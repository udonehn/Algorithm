def solution(n):
    answer = []
    triangle = [[0 for _ in range(i + 1)] for i in range(n)]
    count = 1
    padding = 0
    
    for i in range(n):
        status = i % 3
        if status == 0:
            for j in range(n - i):
                triangle[j + padding + (i // 3)][padding] = count
                count += 1
            padding += 1
        elif status == 1:
            for j in range(n - i):
                triangle[-padding][j + padding] = count
                count += 1
        elif status == 2:
            for j in range(n - i):
                triangle[-(padding + j + 1)][-padding] = count
                count += 1

    for l in triangle:
        answer += l
    return answer