# Користувачем водиться початковий і кінцевий рік.
# Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно).

def vysokosnyi_1(x):
    return x % 400

def vysokosnyi_2_1(x):
    return x % 4
    
def vysokosnyi_2_2(x):
    return x % 100    

start_year = int(input('Введіть початковий рік: ')) 
finish_year = int(input('Введіть кінцевий  рік: '))
print ('Високосні роки:')

for year in range(start_year, finish_year+1):
    if vysokosnyi_2_1(year) == 0 and vysokosnyi_2_2(year) != 0 or vysokosnyi_1(year) == 0:
        print(year)
