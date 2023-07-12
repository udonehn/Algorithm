list = list(input())
list2=[]
num=[]

for i in range(3-(len(list)%3)):
    list.insert(0,'0')

for i in range(int(len(list)/3)):
    list2.append(''.join(list[i*3 : i*3+3]))

for n in list2:
    if n == "000":
        num.append('0')
    elif n == "001":
        num.append('1')
    elif n == "010":
        num.append('2')
    elif n == "011":
        num.append('3')
    elif n == "100":
        num.append('4')
    elif n == "101":
        num.append('5')
    elif n == "110":
        num.append('6')
    elif n == "111":
        num.append('7')

print(int(''.join(num)))