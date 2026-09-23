import random

def run_random_tests(all_tests, count):
    if count > len(all_tests):
        print(f'Ошибка. Доступно {len(all_tests)}')
        return

    selected_tests = random.sample(all_tests,count)

    possible_statuses = ['PASS', 'FAIL','SKIP']
    results = []

    for test in selected_tests:
        status = random.choice(possible_statuses)
        results.append((test,status))

    print ('Отчёт о запуске автотестов')
    for test,status in results:
        print(f'{test} - {status}')
tests = [
    'test_login',
    'test_logout',
    'test_registration',
    'test_profile',
    'test_payment',
    'test_search'
]

try:
    user_count = int(input('Количество тестов для запуска: '))

    run_random_tests(tests,user_count)

except ValueError:
    print('Ошибка. Введите целое число')