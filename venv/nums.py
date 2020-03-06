#Функция приведения вводимого значения к числовому (FLOAT), на входе число, на выходе float
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

#Функция упорядочивания введенного массива, на входе массив, на выходе сортированный массив
def order_elements(sort_arr):
    tmp = 0
    size = len(sort_arr)
    for i in range(1,size):
        for k in range(0, size-i):
            if sort_arr[k] > sort_arr[k+1]:
                tmp = sort_arr[k]
                sort_arr[k] = sort_arr[k+1]
                sort_arr[k + 1] = tmp
                k += 1
                #print (sort_arr) # debug
    return sort_arr

#Запрос чисел, на входе указание кол-ва числе, на выходе массив float значений
def ask_dig(size):
    user_digits = []
    for j in range(size):
        prompted_dig = input(f'Введите число №{j+1}: ')
        user_digits.append(digitalize_prompt(prompted_dig))
    return user_digits

#Выдача результата, на входе сортированный массив
def res_func(user_digits):
    size = len(user_digits)
    print (f'Введено: {user_digits}') # debug
    user_digits = order_elements(user_digits)

    if user_digits[0] < user_digits[round((size-1)/2)] < user_digits[size-1]:
        print(f'Число между Min и Max = {user_digits[round((size-1)/2)]}: ')
    else:
        print('Числа между Min и Max не обнаружено')

if __name__ == '__main__':
    res_func(ask_dig(3))