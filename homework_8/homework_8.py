class Flower:
    def __init__(self, name, cost, lifetime):
        self.name = name
        self.cost = cost
        self.lifetime = lifetime

    def __str__(self):
        return f'{self.name} (ЦЕНА: {self.cost} руб., ВРЕМЯ ЖИЗНИ: {self.lifetime} д.)'


class Rose(Flower):
    def __init__(self):
        super().__init__(name='Роза', cost=150, lifetime=7)


class Tulip(Flower):
    def __init__(self):
        super().__init__(name='Тюльпан', cost=100, lifetime=5)


class Peony(Flower):
    def __init__(self):
        super().__init__(name='Пион', cost=350, lifetime=5)


class Lily(Flower):
    def __init__(self):
        super().__init__(name='Лилия', cost=300, lifetime=10)


class Orchid(Flower):
    def __init__(self):
        super().__init__(name='Орхидея', cost=250, lifetime=14)


class Accessory:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __str__(self):
        return f'Аксессуар: {self.name} ({self.cost} руб.)'

    def __repr__(self):
        return self.__str__()


class Bouquet:
    def __init__(self):
        self.flowers = []
        self.accessories = []

    def add_flower(self, flower):
        self.flowers.append(flower)
        print(f'Добавлен цветок {flower.name}.')

    def add_accessory(self, accessory):
        self.accessories.append(accessory)
        print(f'Добавлен аксессуар {accessory.name}.')

    def get_total_cost(self):
        total_cost = sum(flower.cost for flower in self.flowers)
        total_cost += sum(acc.cost for acc in self.accessories)
        return total_cost

    def get_withering_time(self):
        if not self.flowers:
            return 0
        total_lifetime = sum(flower.lifetime for flower in self.flowers)
        average = total_lifetime / len(self.flowers)
        return round(average, 1)

    def sort_flowers_by_cost(self):
        self.flowers.sort(key=lambda flower: flower.cost)
        print('Сортировка цветов по стоимости выполнена.')

    def find_flower(self, name):
        for flower in self.flowers:
            if flower.name.lower() == name.lower():
                return True
        return False

    def show_bouquet(self):
        print('Букет:')
        if not self.flowers and not self.accessories:
            print('Отсутствуют данные для сбора букета')
            return
        for flower in self.flowers:
            print(f'  {flower}')
        for acc in self.accessories:
            print(f'  {acc}')


print('Сбор букета')
my_bouquet = Bouquet()

my_bouquet.add_flower(Rose())
my_bouquet.add_flower(Tulip())
my_bouquet.add_flower(Peony())
my_bouquet.add_flower(Lily())

my_bouquet.add_accessory(Accessory('Глянцевая упаковка', 50))
my_bouquet.add_accessory(Accessory('Ленточка', 30))

my_bouquet.show_bouquet()

print(f'Итоговая цена букета: {my_bouquet.get_total_cost()} руб.')

print('Время жизни цветов')
print(f'Среднее время жизни цветов в букете: {my_bouquet.get_withering_time()} дней')

print(f'Роз в букете: {my_bouquet.find_flower("Роза")}')
print(f'Лилий в букете: {my_bouquet.find_flower("Лилия")}')
print(f'Пионов в букете: {my_bouquet.find_flower("Пион")}')
print(f'Тюльпанонв в букете: {my_bouquet.find_flower("Тюльпан")}')

print('Сортировка по цене:')
my_bouquet.sort_flowers_by_cost()
for flower in my_bouquet.flowers:
    print(f'  {flower.name} - {flower.cost} руб.')