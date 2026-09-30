def run_test_with_retried(retries, timeout):
    if not isinstance(retries, int) or not (0 <= retries <= 5):
        raise ValueError(f'Количество повторов должно быть целым числом от 0 до 5')
    if timeout < 0:
        raise ValueError(f'Таймаут должен не должен быть отрицательным числом')
    return f'Тест запущен успешно! Повторов: {retries}, Таймаут: {timeout} секунд'

tests = [
    (4, 10),
    (2, -5),
    (6,5),
    (0,0)
]

print('Запускаем тесты')
for i, (retries, timeout) in enumerate(tests, start=1):
    print(f'Попытка {i}: retries={retries}, timeout={timeout}')

    try:
        result = run_test_with_retried(retries, timeout)
        print(result)

    except ValueError as e:
        print(f'Исключение: {e}')

