a=[]
print('Введите количество элементов: ')
n= int(input())
for i in range(n):
    a.append(i+1)
print(a)

print('Введите значение чтобы узнать ближнее значение:')
x= int(input())

for i in range(n):
    if x in a and a[i]>x<a[i-1]:
        print(a[i-1])
        break




