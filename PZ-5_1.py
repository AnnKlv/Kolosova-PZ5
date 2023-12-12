#составить программу, в которой функция генерирует четырехзначное число и определяет, есть ли в числе одинаковые цифры.

import random
def generate_number():
    number = random.randint (1000, 9999) #генерация случайного числа от 1000 до 9999
    return number #возврат сгенерированного числа

def check_repeated_digits(number):
    digits = set() #создание пустого множества для хранения цифр
    for digit in str(number): #перебор цифр в строковом представлении числа
        if digit in digits:  #если цифра уже есть во множестве
            return False #вернуть False, так как есть повторяющиеся цифры
        digits.add(digit) #добавить цифру во множество
    return True #вернуть True, если все цифры уникальны

while True:
    number = generate_number()
    if check_repeated_digits(number): #если нет повторяющихся цифр
        print(f"Сгенерированный номер: {number}") #вывод сгенерированного числа
    else:
        print("Номер содержит повторяющиеся цифры") #вывод сообщения о повторяющихся цифрах