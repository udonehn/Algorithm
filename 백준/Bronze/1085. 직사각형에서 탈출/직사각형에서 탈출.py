x, y, w, h = map(int, input().split())

a = x
if(a>y):
    a=y

if(a>w-x):
    a=w-x

if(a>h-y):
    a=h-y
    
print(a)