# Створити цикл від 0 до ... (вводиться користувачем). 
# В циклі створити умову, яка буде виводити поточне значення, якщо остача від ділення на 17 дорівнює 0.

def operation(x):
    return x % 17

finish_number = int(input('Введіть ціле чило: '))   

for a in range(finish_number+1):
    if not operation(a) == 0:
        continue
    print(a)
