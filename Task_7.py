# Ну і традиційно -> калькулятор :)
# повинна бути 1 ф-ція яка б приймала 3 аргументи
# - один з яких операція, яку зробити!

def calculate(x, y, diya):
    print('Введіть дію:')
    diya = input("Дія: ")
    x = float(input('Введіть x: '))
    y = float(input('Введіть y: '))
    if diya == '+':
        print(x, ' + ', y, ' = ', x + y)
    if diya == '-':
        print(x, ' - ', y, ' = ', x - y)
    if diya == '*':
        print(x, ' * ', y, ' = ', x * y)
    if diya == '/':
        if y != 0:
            print(x, ' / ', y, ' = ', x / y)
        else: 
            print("На нуль ділити не можна!")

a = 0
b = 0
c = ''
result = calculate (a, b, c)            
