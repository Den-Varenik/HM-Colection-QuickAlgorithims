from random import random


def register():
    data = create_dict()
    while True:
        nick_name = input('Придумайте nick_name: ')
        if data.get(nick_name) is None:
            break
        else:
            print('Данный никнейм уже используется')

    log = input('Внимание, в случае утраты пароля, сброс пароля производиться по логину.\n'
                'Никому не передавайте ваши данные!\n'
                'Введите ваш логин: ')
    while True:
        pas = input('Придумайте пароль: ')
        if pas == input('Повторите ваш пароль: '):
            break
        else:
            print('Пароли не совпадают!')

    print(f'Убедитесь в коректности в веденных данных:\n'
          f'------------------------------------------\n'
          f'Nick-name: {nick_name}\n'
          f'Login: {log}\n'
          f'Password: {pas}\n'
          f'------------------------------------------')
    answer = input('Y/N: ')
    if answer == 'Y' or answer == 'y':
        with open('log_and_key.txt', 'a', encoding='utf-8') as file:
            file.write(f'{nick_name} - {log} {pas}\n')
    else:
        register()


def sing_in(nick_name: str):
    data = create_dict()
    if data.get(nick_name) is None:
        print('Такой пользователь не найден. Зарегестрируйтесь')
    else:
        if tuple([input('Login: '), input('Password: ')]) == data.get(nick_name):
            to_search()
        else:
            print('Логин и пароль введены не правильно.\n'
                  'Авторизация не успешна.')


def change_pass(nick_name):
    data = create_dict()
    secret_info = data.get(nick_name)
    if secret_info[0] == input('Введите логин: '):
        pas = input('Введите новый пароль: ')
        while pas != input('Повторите пароль: ') or pas == secret_info[1]:
            print('Пароли не совпадают или совпадает с прошлым паролем.')
            pas = input('Введите новый пароль: ')
        data[nick_name] = tuple([secret_info[0], pas])
        update_dict(data)


def create_dict():
    with open('log_and_key.txt', 'r', encoding='utf-8') as file:
        data = [(i.strip()).split(' - ') for i in file.readlines()]

    # Create dict
    for i in data:
        i[1] = tuple(i[1].split())
    data = dict(data)
    return data


def update_dict(data: dict):
    with open('log_and_key.txt', 'w', encoding='utf-8') as file:
        file.write('')
    with open('log_and_key.txt', 'a', encoding='utf-8') as file:
        for key, item in data.items():
            file.write(f'{key} - {item[0]} {item[1]}\n')


def to_search():
    arr = [int(random() * 100) for i in range(20)]
    arr.sort()
    try:
        x = int(input('Введите искомое число: '))
        s, e = [int(i) for i in input('Введите границы поиска "x - y"\n'
                                      'X ans Y натуральные числа: ').split(' - ')]
        if s > e != -1:
            s, e = e, s
        e = e if len(arr) >= e else -1
        print(search(arr, x, s, e))
    except ValueError:
        print('Введены не верные значения. Программа завершенна.')


def search(arr: list, x, s=0, e=-1) -> str:
    arr = arr[s:e]
    m = int(len(arr)-1/2)
    if x > arr[m]:
        s = m+1
    elif x < arr[m]:
        e = m
    elif x == arr[m]:
        return arr[m]
    return search(arr, x, s, e) if arr[-1] != x and len(arr) > 1 else (arr[-1] if arr[-1] == x else 'Объект не найден')
