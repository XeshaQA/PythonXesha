class InvalidTestStatusError(Exception):
    pass

def check_test_status(status):
    valid_statuses = ['PASS', 'FAIL', 'SKIP']
    if status not in valid_statuses:
        raise InvalidTestStatusError(f'Недопустимый статус: {status}')
    return f'Статус {status} корректен!'
test_statuses = ['PASS', 'FAIL', 'SKIP', 'abc']
for status in test_statuses:
    try:
        result = check_test_status(status)
        print(result)

    except InvalidTestStatusError as e:
        print(f'Ошибка валидации! {e}')
