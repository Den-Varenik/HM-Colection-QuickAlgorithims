from lib.algoritm import *

if __name__ == '__main__':
    while True:
        print('Перед началом работы программы авторизуйтесь.\n'
              '1. Регистрация.\n'
              '2. Вход в систему.\n'
              '3. Смена пароля. \n'
              '0. Выход.')
        try:
            answer = int(input('Выберите вариант: '))
            if answer == 0:
                break
            elif answer == 1:
                register()
            elif answer == 2:
                sing_in(input('Введите nick-name: '))
            elif answer == 3:
                change_pass(input('Введите nick-name: '))
            else:
                print('Вариант не выбран.')
        except ValueError:
            print('Ошибка значения.')
