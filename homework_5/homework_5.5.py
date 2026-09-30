import json
from functools import reduce

def generate_test_report(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError as e:
        print(f"Файл '{input_file}' Не найден!")
        return
    except json.decoder.JSONDecodeError as e:
        print(f"Не удалось прочитать JSON")
        return

    if not isinstance(data, list):
        print('в файле JSON отсутствуют данные')
        return

    try:
        for test in data:
            if (not isinstance(test, dict) or
            'name' not in test or
            'status' not in test or
            'time' not in test):
                raise TypeError(f"Ошибка! некорректная структура: {test}")
    except TypeError as e:
        print(f"Ошибка! {e}")
        return



    statuses = [test['status'] for test in data]

    count_pass = statuses.count('PASS')
    count_fail = statuses.count('FAIL')
    count_skip = statuses.count('SKIP')

    failed_tests = list(map(lambda t: t['name'],
                            filter(lambda t: t['status'] == 'FAIL', data)))

    longest_test = max(data, key=lambda t: t['time'])

    total_time = reduce(
        lambda acc, t: acc + t['time'],
        data,
        0
    )

    report = {
        'total_tests': len(data),
        'status_counts':
            {
                'PASS': count_pass,
                'FAIL': count_fail,
                'SKIP': count_skip
            },

    'failed_tests': failed_tests,
    'longest_test':

    {
        'name': longest_test['name'],
        'time': longest_test['time']
    },
    'total_time': round(total_time, 2)
    }
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(report, file, ensure_ascii=False, indent=4)
        print(f"Отчёт успешно сохранен! Файл '{output_file}'")
    except Exception as e:
        print(f'Ошибка при сохранении! {e}')


if __name__ == '__main__':
    generate_test_report('test_result.json', 'report.json')