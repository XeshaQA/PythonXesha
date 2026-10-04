import functools

def retry(count):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, count + 1):
                print(f'Запуск теста #{attempt}')
                result = func(*args, **kwargs)

                if result is True:
                    print(f'Успешно. Попыток: {count}')
                    return True




            print(f'Тест провален. Попыток: {count}')
            return False
        return wrapper
    return decorator

attempts_1 = []

@retry(count=2)
def flaky_test_1():
    attempts_1.append(1)
    if len(attempts_1) == 2:
        return True
    return False
print('TEST #1 PASSED')
flaky_test_1()

@retry(count=3)
def always_fail_test():
    return False
print('TEST #2 FAILED')
always_fail_test()

@retry(count=3)
def test_with_args(a, b, name='TEST'):
    print(f'Выполнен с аргументами: а={a}, b={b}, name={name}')
    return a + b > 100
print ('Тест 3 с аргументами')
test_with_args(15, 30, name='Проверка')
test_with_args(70,40)