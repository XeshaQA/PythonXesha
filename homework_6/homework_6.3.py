import functools
def log_test(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Запуск теста: {func.__name__}')

        result = func(*args, **kwargs)
        print(f'Тест {func.__name__} завершен')
        print(f'Результат: {result}')

        return result
    return wrapper

@log_test
def test_sum(a, b):
    return a + b
@log_test
def test_status(status, message='OK'):
    return (f'Статус: {status}, Сообщение: {message}')

print('Запуск тестов #1')
test_sum(10, 20)

print('Запуск тестов #2')
test_status(status='PASSED', message='OK')