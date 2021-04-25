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
    i = 0
    list_nick = list(list_u.keys())
    print('Список пользователей:')
    for i in range(len(list_nick)):
        print("{}. {}".format(i + 1, list_nick[i]))

def info_user():
    nickname = input('Введите никнейм пользователя: ')
    infolist = list_u.get(nickname, False)
    if infolist != False:
        print('Для пользователя {} сохранены следующие данные:\nрост - {} см, '\
            'вес - {} кг'.format(infolist[0], infolist[1], infolist[2]))
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
    key = input('Введите никнейм пользователя, данные которого хотите изменить'\
        ': ')
    if key in list_u.keys():
        infolist = [input('Введите имя: '), int(input('Введите рост (см): ')), \
            int(input('Введите массу тела (кг): '))]
        list_u.update({key: infolist})
    else:
        print('Никнейм не определен')
        return

def delete_user():
    key = input('Введите никнейм пользователя, данные которого хотите удалить:'\
        ' ')
    if key in list_u:
        list_u.pop(key)
    else:
        print('Никнейм не определен')
        return

def add_user():
    key = input('Для создания пользователя введите никнейм: ')
    infolist = [input('Введите имя: '), int(input('Введите рост (см): ')), \
    int(input('Введите массу тела (кг): '))]
    list_u.update({key: infolist})

ACTIONS = {
    1: list_users,
    2: info_user,
    3: create_user,
    4: delete_user,
    5: add_user,
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
    else:
        print('Вы выполнили выход из программы')

main()
