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

def quad(arr, N):
    r = check(arr, N)
    if r == '1':
        return '1'
    elif r == '0':
        return '0'
    else:
        index = int(N/2)
        ans = '('
        ans+= quad([arr[:index] for arr in arr[:index]],index)
        ans+= quad([arr[index:] for arr in arr[:index]],index)
        ans+= quad([arr[:index] for arr in arr[index:]],index)
        ans+= quad([arr[index:] for arr in arr[index:]],index)
        ans+=')'
        return ans
    
N = int(input())
arr=[]

for i in range(N):
    arr.append(list(input()))
print(quad(arr, N))