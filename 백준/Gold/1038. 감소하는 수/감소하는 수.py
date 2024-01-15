result = []

def combination(arr, n, last):
    if len(arr) == n:
        return arr
    for i in range(last+1, 10):
        temp = combination(arr+[i], n, i)
        if temp:
            temp.reverse()
            string=''
            for i in temp:
                string+=str(i)
            result.append(int(string))


if __name__ == "__main__":
    for i in range(1, 11):
        combination([], i, -1)
    result.sort()
    n = int(input())
    if n >= len(result):
        print(-1)
    else:
        print(result[n])