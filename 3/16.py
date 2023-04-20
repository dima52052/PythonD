n = int(input('Введите длину массива: '))
ai  = [i+1 for i in range(n)]
print(ai)
x = int(input('Найти: '))
print(ai.count(x)) #выводим количество вхождений
