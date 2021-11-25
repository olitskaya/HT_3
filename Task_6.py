# Маємо рядок -->
# "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00
# koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" ->
# просто потицяв по клаві.
# Створіть ф-цію, яка буде отримувати рядки на зразок цього,
# яка оброблює наступні випадки:
# - якщо довжина рядка в діапазоні 30-50 ->
# прінтує довжину, кількість букв та цифр
# - якщо довжина менше 30 ->
# прінтує суму всіх чисел та окремо рядок без цифр (лише з буквами)
# - якщо довжина більше 50 -> ваша фантазія

def perevirka(a):
    dovzhyna = len(a)
    if 29 < dovzhyna < 51 :
        print('Довжина рядка: ', len(a))
        d = {'Букви': 0, 'Цифри': 0}
        for i in a:
            if i.isalpha():
                d['Букви'] += 1
            if i.isdigit():
                d['Цифри'] += 1
        print('Кількість цифр: ', d['Цифри'], 'Кількість букв: ', d['Букви'])
    if dovzhyna < 30:
        sum = 0
        for x in a:
            if x.isdigit() == True:
                z = int(x)
                sum = sum + z
        print('Сума всіх цифр: ', sum)
        b = ''  
        for c in a:  
            if c.isalpha():  
                b = b + c
        print('Рядок без цифр і символів: ', b)        
    if dovzhyna > 50 :
        print('Гарного дня!')
    return

ryadok = str(input('Введіть рядок: '))
perevirka(ryadok)
