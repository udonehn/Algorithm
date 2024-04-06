import sys
input = lambda: sys.stdin.readline().rstrip()


def get_distance(a, b):
    cnt = 0
    for i in range(4):
        if a[i] != b[i]:
            cnt += 1
    return cnt


def solve(N, mbti):
    if N > 32:
        return 0
    answer = sys.maxsize
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                count = 0
                count += get_distance(mbti[i], mbti[j])
                count += get_distance(mbti[j], mbti[k])
                count += get_distance(mbti[k], mbti[i])
                answer = min(answer, count)
    return answer


if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        mbti = input().split()
        print(solve(N, mbti))
