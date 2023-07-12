def check(arr, n):
    if arr[0][0]=='0':
        s = '0'
    else:
        s = '1'
    for i in range(n):
        for j in range(n):
            if arr[i][j] != s:
                return -1
    return s

def quad(arr, N, ans):
    r = check(arr, N)
    if r == '1':
        ans[1]+=1
        return (ans)
    elif r == '0':
        ans[0]+=1
        return (ans)
    else:
        index = int(N/2)
        ans = quad([arr[:index] for arr in arr[:index]],index, ans)
        ans = quad([arr[index:] for arr in arr[:index]],index, ans)
        ans = quad([arr[:index] for arr in arr[index:]],index, ans)
        ans = quad([arr[index:] for arr in arr[index:]],index, ans)
        return ans
    
N = int(input())
arr=[]

for i in range(N):
    arr.append(input().split())
ans = quad(arr, N, [0,0])

print('{}\n{}'.format(ans[0],ans[1]))