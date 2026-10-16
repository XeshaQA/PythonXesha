class ATM:
    def __init__(self, count_20, count_50, count_100):
        self.count_20 = count_20
        self.count_50 = count_50
        self.count_100 = count_100
    def add_money(self, add_20, add_50, add_100):
        self.count_20 += add_20
        self.count_50 += add_50
        self.count_100 += add_100
        print('Счёт банкомата пополнен успешно!')
    def withdraw(self, amount):
        if amount % 10 != 0:
            print('Сумма должна быть кратна числу 10!')
            return False

        temp_100 = self.count_100
        temp_50 = self.count_50
        temp_20 = self.count_20

        give_100 = min(amount // 100, temp_100)
        amount -= give_100 * 100
        temp_100 -= give_100

        give_50 = min(amount // 50, temp_50)
        amount -= give_50 * 50
        temp_50 -= give_50

        give_20 = min(amount // 20, temp_20)
        amount -= give_20 * 20
        temp_20 -= give_20

        if amount != 0:
            print('Недостаточно купюр нужного номинала! Невозможно выдать деньги')
            return False

        self.count_100 = temp_100
        self.count_50 = temp_50
        self.count_20 = temp_20

        print(f'Выдано: {give_100} купюр по 100 рублей, {give_50} купюр по 50 рублей, {give_20} купюр по 20 рублей')
        return True
atm = ATM(count_20=5,count_50=2, count_100=3)
atm.add_money(add_20=10, add_50=10, add_100=10)
print('Попытка снять 270 рублей:')
result = atm.withdraw(270)
print(f'Результат: {result}')

print('Попытка снять 260 рублей:')
result = atm.withdraw(260)
print(f'Результат: {result}')


print('Попытка снять 10000:')
result = atm.withdraw(10000)
print(f'Результат: {result}')
