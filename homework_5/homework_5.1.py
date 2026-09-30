from functools import reduce

tests = [
    {"name": "test_1", "status": "PASS", "time": 0.5},
    {"name": "test_2", "status": "FAIL", "time": 1.05},
    {"name": "test_3", "status": "SKIP", "time": 0.046456},
    {"name": "test_4", "status": "PASS", "time": 30.5},
    {"name": "test_5", "status": "FAIL", "time": 5.0}
]

statuses = [t['status'] for t in tests]
count_pass = statuses.count('PASS')
count_fail = statuses.count('FAIL')
count_skip = statuses.count('SKIP')

print(f'Количетсво тестов со статусом PASS: {count_pass}')
print(f'Количество тестов со статусом FAIL: {count_fail}')
print(f'Количетсво тестов со статусом SKIP: {count_skip}')

failed_tests = list(filter(lambda t: t['status'] == 'FAIL', tests))
failed_names = list(map(lambda t: t['name'], failed_tests))
print(f'Список упавших тестов: {failed_names}')



passed_tests = [t['name'] for t in tests if t['status'] == 'PASS']
print(f'Успешные тесты: {passed_tests}')
total_time = reduce(
    lambda acc, t: acc + t['time'],
    tests,
    0
)
print(f'Общее время: {total_time}')