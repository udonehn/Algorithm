def check(arr, n):
    if arr[0][0]=='0':
        s = '0'
    elif arr[0][0]=='1':
        s = '1'
    elif arr[0][0]=='-1':
        s = '-1'
    for i in range(n):
        for j in range(n):
            if arr[i][j] != s:
                return -1
    return s

def quad(arr, N, ans):
    r = check(arr, N)
    if r == '1':
        ans[1]+=1
    elif r == '0':
        ans[0]+=1
    elif r == '-1':
        ans[2]+=1
    else:
        index = int(N/3)
        for i in range(0,N,index):
            for j in range(0,N,index):
                ans = quad([arr[j:j+index] for arr in arr[i:i+index]],index, ans)

    return ans
    
N = int(input())
arr=[]

for i in range(N):
    arr.append(input().split())

ans = quad(arr, N, [0,0,0])

print('{}\n{}\n{}'.format(ans[2],ans[0],ans[1]))