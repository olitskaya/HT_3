# Написати функцію season, яка приймає один аргумент - номер місяця (від 1 до 12), яка буде повертати пору року, якій цей місяць належить (зима, весна, літо або осінь).

def season(x):
    if 0 < x < 3 or x == 12:
        y = 'Зима'
    if 2 < x < 6:
        y = 'Весна'
    if 5 < x < 9:
        y = 'Літо'
    if 8 < x < 12:
        y = 'Осінь'
    return y    
        
month = int(input('Введіть номер місяця: '))
print ('Пора року: ', season(month))
