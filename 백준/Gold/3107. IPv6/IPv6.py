import sys
input = lambda: sys.stdin.readline().rstrip()


if __name__ == "__main__":
    ip = input().split(':')
    for i in range(len(ip)):
        if 1 <= len(ip[i]) < 4:
            ip[i] = '0' * (4 - len(ip[i])) + ip[i]

    if ip[0] == '':
        ip.pop(0)
    if ip[-1] == '':
        ip.pop(-1)

    for i in range(len(ip)):
        if len(ip[i]) == 0:
            ip.pop(i)
            for _ in range(8 - len(ip)):
                ip.insert(i, '0000')

    for i in range(len(ip)):
        if len(ip[i]) == 0:
            ip[i] = '0000'

    print(':'.join(ip))
