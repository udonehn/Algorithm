import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()
answer = {'1': (0, 0), '2': (1, 0), '3': (2, 0), '4': (0, 1), '5': (1, 1), '6': (2, 1), '7': (0, 2), '8': (1, 2)}

def find_space(arr):
    for y in range(3):
        for x in range(3):
            if arr[y][x]=='0':
                return x,y

def copy_puzzle(puzzle):
    arr=[]
    for i in range(3):
        arr.append([j for j in puzzle[i]])
    return arr

def make_string(puzzle):
    result=''
    for i in range(3):
        for j in range(3):
            result+=puzzle[i][j]
    return result

def get_h_score(arr):
    result=0
    for y in range(3):
        for x in range(3):
            number=arr[y][x]
            if number=='0':
                continue
            answer_x, answer_y = answer[number]
            if x-answer_x<0:
                result+=-(x-answer_x)
            else:
                result+=x-answer_x
            if y-answer_y<0:
                result+=-(y-answer_y)
            else:
                result+=y-answer_y
    return result

def insert_heap(copy, g_score, visited, heap):
    h_score = get_h_score(copy)
    f_score = h_score + g_score + 1

    string_puzzle=make_string(copy)
    if string_puzzle not in visited:
        visited.add(make_string(copy))
        heappush(heap, (f_score, g_score + 1, copy))

def solve(arr):
    heap=[(get_h_score(arr),0,arr)]
    visited=set()

    while heap:
        f_score,g_score,puzzle=heappop(heap)    # f(x)=h(x)+g(x), g(x), puzzle
        if f_score==g_score:    #h(x)==0
            return g_score

        x,y=find_space(puzzle)
        if y!=0:    #상
            copy=copy_puzzle(puzzle)
            copy[y][x], copy[y-1][x] = copy[y-1][x], copy[y][x]
            insert_heap(copy, g_score, visited, heap)

        if y!=2:    #하
            copy=copy_puzzle(puzzle)
            copy[y][x], copy[y+1][x] = copy[y+1][x], copy[y][x]
            insert_heap(copy, g_score, visited, heap)

        if x!=0:    #좌
            copy=copy_puzzle(puzzle)
            copy[y][x], copy[y][x-1] = copy[y][x-1], copy[y][x]
            insert_heap(copy, g_score, visited, heap)

        if x!=2:    #우
            copy=copy_puzzle(puzzle)
            copy[y][x], copy[y][x+1] = copy[y][x+1], copy[y][x]
            insert_heap(copy, g_score, visited, heap)

    return -1


if __name__ == "__main__":
    arr = []
    for _ in range(3):
        arr.append(input().split())
    print(solve(arr))