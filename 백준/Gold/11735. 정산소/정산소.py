import sys
input = lambda :sys.stdin.readline().rstrip()

def result(line, deleted, n):
    res = (line+1+line+n)/2*n
    res = res - sum(deleted) - len(deleted)*line
    return int(res)

if __name__=="__main__":
    n, q = map(int, input().split())
    deleted_row=[]
    deleted_column=[]
    deleted_row_check=[False for _ in range(n+1)]
    deleted_column_check=[False for _ in range(n+1)]

    for _ in range(q):
        query = input().split()
        number = int(query[1])
        if query[0]=="R":
            if not deleted_row_check[number]:
                deleted_row.append(number)
                deleted_row_check[number]=True
                print(result(number, deleted_column, n))
            else:
                print(0)
        else:
            if not deleted_column_check[number]:
                deleted_column.append(number)
                deleted_column_check[number]=True
                print(result(number, deleted_row, n))
            else:
                print(0)