class CreditCard:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f'Счет был пополнен на {amount}. Текущий баланс: {self.balance}')
        else:
            print('Сумма пополнения не может быть отрицательным числом!')

    def withdraw(self, amount):
        if amount > self.balance:
            print('На счете недостаточно средств')
        elif amount <= 0:
            print('Сумма снятия не может быть отрицательным числом!')
        else:
            self.balance -= amount
            print(f'Снято {amount}. Баланс: {self.balance}')

    def show_info(self):
        print(f'Номер счёта: {self.account_number}')
        print(f'Баланс: {self.balance}')
my_card = CreditCard('1234-5678-9101', 1000)

print('Информация:')
my_card.show_info()

print('Пополнение счёта: ')
my_card.deposit(1000)

print('Снятие со счёта: 5000')
my_card.withdraw(5000)

print('Итого:')
my_card.show_info()

