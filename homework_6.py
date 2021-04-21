def show_menu():
    menu = """
    МЕНЮ:
    1. Список пользователей
    2. Посмотреть информацию о пользователе
    3. Изменить данные о пользователе
    4. Удалить пользователя
    5. Добавить пользователя
    6. Выход
    """
    print(menu)
    return int(input('Ваш выбор: '))

def list_users():
#    while True:
    print(list_u.keys())
    

def info_user():
    nickname = input('Введите никнейм пользователя: ')
    infolist = list_u.get(nickname, False)
    if infolist != False:
        print('Для пользователя ', infolist[0], ' сохранены следующие данные:\n'
        'рост - ', infolist[1], ' см, вес - ', infolist[2], ' кг')
        bmi = infolist[2] / (infolist[1] / 100)  ** 2
        st = (50 - 10) / 20
        x = int((bmi - 10) / st)
        y = int((50-10) / st - x - 1)
        print('Индекс массы тела: ', round(bmi, 2))
        print('10' + ('=' * x) + '|' + ('=' * y) + '50')
    else:
        print('Никнейм не определен')
        return

def create_user():
    key = input('Введите никнейм пользователя, данные которого хотите изменить: ')
    key_bool = key in list_u
    if key_bool == True:
        infolist = [input('Введите имя: '), input('Введите рост (см): '), \
            input('Введите массу тела (кг): ')]
        list_u.update({key: infolist})
#        print(list_u)
    else:
        print('Никнейм не определен')
        return

def delete_user():
    key = input('Введите никнейм пользователя, данные которого хотите удалить: ')
    key_bool = key in list_u
    if key_bool == True:
        list_u.pop(key)
#        print(list_u)
    else:
        print('Никнейм не определен')
        return

def add_user():
    key = input('Для создания пользователя введите никнейм: ')
    infolist = [input('Введите имя: '), input('Введите рост (см): '), \
    input('Введите массу тела (кг): ')]
    list_u.update({key: infolist})
#    print(list_u)

ACTIONS = {
    1: list_users,
    2: info_user,
    3: create_user,
    4: delete_user,
    5: add_user,
#    6: exit_prog,
}

list_u = {
    'nick1' : ['Andrei', 180, 70],
    'nick2' : ['Oleg', 177, 82],
    'nick3' : ['Ivan', 185, 91],
}

def select_action(answer: int):
    return ACTIONS.get(answer, show_menu)

def main():
    answer = 0
    while answer != 6:
        action = select_action(answer)
        answer = action()

main()
