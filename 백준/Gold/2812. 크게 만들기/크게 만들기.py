def solve(N, K, number):
    count = 0
    stack = []
    for num in number:
        while count < K and stack and stack[-1] < num:
            stack.pop()
            count += 1
        stack.append(num)
    for _ in range(K - count):
        stack.pop()

    return ''.join(list(map(str, stack)))


if __name__ == "__main__":
    N, K = map(int, input().split())
    number = list(map(int, list(input())))
    print(solve(N, K, number))