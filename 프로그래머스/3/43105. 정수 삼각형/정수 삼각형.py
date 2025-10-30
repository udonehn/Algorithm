def solution(triangle):
    height = len(triangle)
    
    if height == 1:
        return triangle[0][0]
    
    for i in range(1, height):
        triangle[i][0] = triangle[i][0] + triangle[i - 1][0]
        triangle[i][-1] = triangle[i][-1] + triangle[i - 1][-1]
    
    for i in range(2, height):
        for j in range(1, i):
            triangle[i][j] = triangle[i][j] + max(triangle[i - 1][j - 1], triangle[i - 1][j])
    
    return max(triangle[-1])