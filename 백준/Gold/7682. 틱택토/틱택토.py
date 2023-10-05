import sys
input = lambda : sys.stdin.readline().rstrip()



def o_and_x_count_valid(ttt, status, x, o):
    if status == "X":
        if x > o:
            return "valid"
        else:
            return "invalid"
    else:
        if x == o:
            return "valid"
        else:
            return "invalid"


def solve(ttt):
    o=0
    x=0
    dot=0
    status = None

    for i in ttt:
        if i=="O":
            o+=1
        elif i=="X":
            x+=1
        else:
            dot+=1

    if not 0<=x-o<=1:
        return "invalid"

    for i in range(3):
        if (ttt[i*3]==ttt[i*3+1]==ttt[i*3+2]) and (ttt[i*3]!="."):
            if status==None:    #같은 줄이 두 번 나오는지 체크
                status=ttt[i*3]
            elif status!=ttt[i*3]:
                return "invalid"

        if (ttt[i]==ttt[i+3]==ttt[i+6]) and (ttt[i]!="."):
            if status==None:
                status=ttt[i]
            elif status != ttt[i]:
                return "invalid"


    if (ttt[0]==ttt[4]==ttt[8] or ttt[2]==ttt[4]==ttt[6]) and (ttt[4]!="."):
        if status == None:
            status = ttt[4]
        elif status != ttt[4]:
            return "invalid"

    if status != None:  #한 줄이 나왔다면 OX 개수가 유효한지 체크
        return o_and_x_count_valid(ttt, status, x, o)


    if dot==0:  #더 이상 빈칸이 없는지 체크
        return "valid"

    return "invalid"


if __name__ == "__main__":
    while True:
        test = input()
        if test == "end":
            break
        print(solve(list(test)))