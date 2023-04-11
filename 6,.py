bilet = [int(i) for i in input('Введите номер билета: ')]
if sum(bilet[:3]) == sum(bilet[3:]):
    print('Yes')
else:
    print('No')