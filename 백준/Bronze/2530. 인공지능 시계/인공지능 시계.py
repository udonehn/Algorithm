h,m,s=map(int,input().split())
time=int(input())
s+=time

if s>=60:
    m+=s//60
    s=s%60
if m>=60:
    h+=m//60
    m=m%60
while h>=24:
    h-=24
print(h,m,s)