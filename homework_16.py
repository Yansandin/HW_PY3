a=[]
count = 0
print('Введите количество элементов: ')
n= int(input())
for i in range(n):
    a.append(i+1)
print(a)

print('Введите значение чтобы узнать сколько раз оно встречается:')
x= int(input())

if x in a:
    count+=1

print(count)
        
