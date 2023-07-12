N, k =map(int, input().split())
coin=[]
for _ in range(N):
    coin.append(int(input()))
many = 0
for i in reversed(coin):
    if k>=i:
        many+=k//i
        k-=(k//i)*i
print(many)