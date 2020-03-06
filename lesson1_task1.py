num = input("Введите число: ")

def is_digit(num):
    if num.isdigit():
       return float(num)
    else:
        try:
            float(num)
            return float(num)
        except ValueError:
            print('Неверный ввод числа')
            exit(0)

numm = is_digit(num)

ans = input('Для перевода в байты введите "b", для перевода в килобайты "k": ')
ans = ans.lower()

if ans == 'b':
    print(f'{numm} Кб = {numm * 1024} байт')
elif ans == 'k':
    print(f'{numm} байт = {numm / 1024} Кбайт')
else:
    print('Неверный ввод')