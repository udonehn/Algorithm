import sys
입력 = lambda: sys.stdin.readline().rstrip()

def 사용가능한숫자리스트찾기(스도쿠, y, x):
    사용가능한숫자리스트 = [True] * 10
    for i in range(9):
        사용가능한숫자리스트[스도쿠[y][i]] = False
        사용가능한숫자리스트[스도쿠[i][x]] = False

    구역중첫번째X값 = x // 3 * 3
    구역중첫번째Y값 = y // 3 * 3
    for i in range(3):
        for j in range(3):
            사용가능한숫자리스트[스도쿠[구역중첫번째Y값 + i][구역중첫번째X값 + j]] = False
    return 사용가능한숫자리스트

def 미완성칸찾기(스도쿠):
    for y in range(9):
        for x in range(9):
            if 스도쿠[y][x]==0:
                return (x, y)
    return False

def 답안지(스도쿠):
    미완성칸좌표 = 미완성칸찾기(스도쿠)
    if not 미완성칸좌표:
        return True
    x, y = 미완성칸좌표

    사용가능한숫자리스트 = 사용가능한숫자리스트찾기(스도쿠, y, x)
    사용가능한숫자수셈=0
    for i in range(1, 10):
        if 사용가능한숫자리스트[i]:
            사용가능한숫자수셈+=1
            스도쿠[y][x] = i
            종료여부 = 답안지(스도쿠)
            if 종료여부:
                return 종료여부
    스도쿠[y][x] = 0


if __name__ == "__main__":
    스도쿠 = []
    for _ in range(9):
        스도쿠.append(list(map(int, list(입력()))))
    답안지(스도쿠)
    for i in 스도쿠:
        print("".join(list(map(str, i))))