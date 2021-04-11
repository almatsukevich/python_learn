print('Калькулятор индекса массы тела')
m = float(input('Введите массу тела (кг) - '))
h = float(input('Введите рост (см) - ')) / 100
i = m / h ** 2
min = int(10)
max = int (50)
if min < i < max:
    l = max - min
    st = l / 20
    x = int((i - min) / st)
    y = int(l / st - x -1)
    print('Ваш индекс массы тела: ', round(i, 2))
    s_out = str(min) + ('=' * x) + '|' + ('=' * y) + str(max)
    print(s_out)
else:
    print('Индекс массы тела находится за пределами диапазона действительных значений. Возможно, Вы ввели недостоверные данные')