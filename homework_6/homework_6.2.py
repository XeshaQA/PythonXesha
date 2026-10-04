def create_time_checker(max_time):
    def check_time(actual_time):
        if actual_time > max_time:
            print(f'Лимит превышен. Указанное время: [{actual_time}] секунд. Лимит: [{max_time}] секунд')
        else:
            print(f'Ура, успешно!! Указанное время: [{actual_time}] секунд. Лимит: [{max_time}] секунд')
    return check_time

check_fast = create_time_checker(5)
check_slow = create_time_checker(10)

print('Тест #1 - лимит 5 секунд:')
check_fast(3)
check_fast(8)

print('Тест #2 - лимит 10 секунд):')

check_slow(3)
check_slow(15)
