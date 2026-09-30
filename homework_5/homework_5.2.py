import json

def process_users_file(filepath: str):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)

    except FileNotFoundError as e:
        print(f"Файл '{filepath}' не найден: {e}")
        return
    except json.JSONDecodeError as e:
        print(f"Не удалось прочитать файл {e}")
        return

    if not isinstance(data, list):
        print("В файле отсутствует информация о пользователях")
        return

    for index, user in enumerate(data, start=1):
        try:
            login = user['login']
            password = user['password']
            expected = user['result']

            print(f"Пользователь {index}:")
            print(f"Логин: {login}")
            print(f"Результат: {expected}")

        except KeyError as e:
            print(f"Ошибка в данных пользователя {index}: Обязательное поле не заполнено: {e}")

if __name__ == '__main__':
    process_users_file("users.json")