# Користувач вводить змінні "x" та "y" з довільними цифровими значеннями;
# Створіть просту умовну конструкцію (звісно вона повинна бути в тілі функції),
# під час виконання якої буде перевірятися рівність змінних "x" та "y" і при нерівності змінних у відповідь повертали різницю чисел.
# Повинні опрацювати такі умови:
# x > y; відповідь - x більше ніж y на z
# x < y; відповідь - y більше ніж x на z
# x == y; відповідь - x дорівнює y

def perevirka(a, b):
    if x > y:
        print('x більше ніж y на ', x - y)
    if x < y:
        print('y більше ніж x на ', y - x)
    if x == y:
        print('x дорівнює y')
    return

x = int(input('Введіть перше число: '))
y = int(input('Введіть друге число: '))
perevirka(x, y)
