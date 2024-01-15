if __name__=="__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    answer=dict()
    for number in arr:
        answer[number] = 0

    eratos=dict()
    for i in range(1000001):
        eratos[i]=[]

    for number in arr:
        i=1
        while i*number<1000001:
            eratos[i*number].append(number)
            i+=1


    for number in arr:
        for winner in eratos[number]:
            if winner == number:
                continue
            answer[winner] += 1
            answer[number] -= 1

    for number in arr:
        print(answer[number], end=' ')