x = int(input('Введите трезначное число: '))
def summa(x):
    summ = 0
    for i in str(x):
        summ += int(i)
    return summ

print(f'Сумма чисел равна {summa(x)}')