if __name__=="__main__":
    xdict=dict()
    ydict=dict()
    for _ in range(3):
        x, y = map(int, input().split())
        if x in xdict:
            xdict[x]+=1
        else:
            xdict[x]=1

        if y in ydict:
            ydict[y]+=1
        else:
            ydict[y]=1

    for k, v in xdict.items():
        if v == 1:
            print(k, end=' ')
    for k, v in ydict.items():
        if v == 1:
            print(k, end=' ')

