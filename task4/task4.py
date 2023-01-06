# Реализуйте алгоритм перемешивания списка
ran = []
for i in range(5):
    n = int(input('Введите число: '))
    ran.append(n)
print(*ran)
import random
random.shuffle(ran)
print(*ran)