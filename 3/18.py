n = int(input('Введите длину массива: '))
ai  = [i+1 for i in range(n)]
print(ai)
x = int(input('Найти: '))
print(min(ai, key=lambda a:abs(a-x)))
