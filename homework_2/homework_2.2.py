password_correct = 'Python123'

for attempt in range(1,4):
    password = input(f'Попытка {attempt} из 3. Введите пароль:')

    if password == password_correct:
        print('Ура победа авторизация успешна!')
        break
    else:
        print('Пароль неверный')
        if attempt == 3:
            print ('Попытки закончились. Блокировка доступа')