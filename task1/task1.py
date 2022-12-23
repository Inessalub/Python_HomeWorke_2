number = input('Введите вещественное число: ')
k = 0
for i in str(number):
    if i != '.':
        k += int(i)
print(k)