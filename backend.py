from random import randint
import itertools

# Задача 1. Даны два списка, нужно вернуть элементы, которые есть в 1-ом списке, но нет во 2-ом. Оценить эффективность своего решения.
a = [randint(-10, 10) for x in range(20)]
b = [randint(-15, 15) for x in range(15)]
print(a)
print(b)

# Эффективность O(n)*O(m), где n - длина списка a, m - длина списка b
c = [x for x in a if x not in b]
print("Результат: сравнения",c)

print()

#Задача 2. Дан массив целых чисел. Нужно удалить из него нули. Можно использовать только О(1) дополнительной памяти.
a = [randint(-3, 3) for x in range(20)]
print(a)
print("Без нулей:", list(filter(lambda x: x != 0, a)))