secret = 37
attempts = 0



while True:
    guess = int(input('Введите число:'))
    attempts += 1
    if guess < secret:
        print('Число должно быть больше')
    elif guess > secret :
        print ('Число должно быть меньше')
    else:

        print('Ура победа')
        print(f'Количество попыток: {attempts}')
        break