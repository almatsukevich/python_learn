name = input('Введите логин: ')
sum_i = 12535.5

def decor(func):
    def name_admin(n, s):
        if n != 'admin':
            return print('Доступ запрещен')
        value = func(s)
        return value
    return name_admin

#@decor
def print_sum(x1):
    print(f'На Вашем счете - {x1} USD')

print_sum(name, sum_i)
