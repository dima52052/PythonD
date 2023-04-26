a = int(input('Введите A: '))
b = int(input('Введите B: '))

def power(a, b):
    if (b == 1):
        return (a)
    if (b != 1):
        return (a * power(a, b - 1))

print(power(a,b))