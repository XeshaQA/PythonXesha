tests = int(input('количество автотестов:'))

pass_count = 0
skip_count = 0
fail_count = 0

for x in range(1, tests + 1):
    status = input(f'результат теста {x}: ')

    if status == 'PASS':
        pass_count += 1
    elif status == 'FAIL':
        fail_count += 1
    elif status == 'SKIP':
        skip_count += 1
    else:

        print('пропуск теста')
        continue
print('Статистика:')
print(f'PASS: {pass_count}')
print(f'FAIL: {fail_count}')
print(f'SKIP: {skip_count}')

if fail_count > 0:
    print(f'Количество упавших тестов: {fail_count}')
else:
    print('Тесты пройдены упешно')
