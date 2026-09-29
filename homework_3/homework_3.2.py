def print_report(test_cases, statuses):
    print('отчёт')
    for case, status in zip(test_cases,statuses):
        print(f'{case} - {status}')

    fail_count = statuses.count('FAIL')
    pass_count = statuses.count('PASS')

    return pass_count, fail_count

test_cases = ['Login', 'Registration', 'Checkout', 'Logout']
statuses = ['PASS', 'FAIL', 'PASS', 'SKIP']

pass_count, fail_count = print_report(test_cases, statuses)

print('Итоги')
print(f'Успешных тестов: {pass_count}')
print(f'(Провальных тестов: {fail_count})')

if fail_count > 0:
    print('Статус: FAIL (есть провальные тесты)')
else:
    print('Статус: PASS')