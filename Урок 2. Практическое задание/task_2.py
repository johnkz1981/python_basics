"""
Задание 2. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

Пример:
Введите целые числа через пробел: 1 2 3 4
Результат: 2 1 4 3

Введите целые числа через пробел: 1 2 3
Результат: 2 1 3
"""
ls = '1 8 3 4 6 8 9'
ls = ls.split()

for v in range(0, len(ls), 2):

    if v + 1 < len(ls):
        print(ls[v], ls[v+1])
        var1, var2 = ls[v], ls[v+1]
        ls[v], ls[v+1] = var2, var1

print(ls)
