size = 3 # вводится набор чисел

#Функция приведения вводимого значения к числовому (FLOAT)
def digitalize_prompt(num):
    if num.isdigit():
       return float(num)
    else:
        try:
            float(num)
            return float(num)
        except ValueError:
            print('Неверно введено число')
            exit(0)

#Функция упорядочивания введенного массива
def order_elements(sort_arr):
    i = 1
    tmp = 0
    while i < size:
        k = 0
        while k < size-i:
            if sort_arr[k] > sort_arr[k+1]:
                tmp = sort_arr[k]
                sort_arr[k] = sort_arr[k+1]
                sort_arr[k + 1] = tmp
                k += 1
                #print (sort_arr) # debug
            else:
                k += 1
        i += 1
    return sort_arr

#Запрос чисел
j=0
user_digits = []
while j < size:
    prompted_dig = input(f'Введите число №{j+1}: ')
    user_digits.append(digitalize_prompt(prompted_dig))
    j += 1

#Выдача результата
print (f'Введено: {user_digits}') # debug
user_digits = order_elements(user_digits)

if user_digits[0] < user_digits[round((size-1)/2)] < user_digits[size-1]:
    print(f'Число между Min и Max = {user_digits[round((size-1)/2)]}: ')
else:
    print('Числа между Min и Max не обнаружено')