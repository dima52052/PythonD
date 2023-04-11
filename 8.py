n= int(input('Введите размер шоколадки n '))
m= int(input('Введите размер шоколадки m '))
k= int(input('Сколько хотите отломить k '))
if k%n == 0 or k%m == 0:
    print('Yes')
else: print('No')