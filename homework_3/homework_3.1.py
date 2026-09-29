def get_test_statistics(results):
     stats = {
        'PASS': 0,
        'FAIL': 0,
        'SKIP': 0,
        'Всего': len(results)
    }

     for result in results:
         if result in stats:
             stats[result] += 1
     return stats

user_input = input('Введите результаты тестов (через пробел): ')

results_list = user_input.split()
statistics = get_test_statistics(results_list)

print(f'Всего тестов: {statistics["Всего"]}')
print(f'PASS: {statistics["PASS"]}')
print(f'FAIL: {statistics["FAIL"]}')
print(f'SKIP: {statistics["SKIP"]}')

if statistics['Всего'] > 0:
    success_rate = (statistics['PASS'] / statistics['Всего']) * 100
    print(f'Успешно: {success_rate:.1f}%')
else:
    print('Успешно: 0.0%')