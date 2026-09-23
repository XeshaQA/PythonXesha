numbers = []
with open('file_1.txt', 'r') as file:
    for line in file:
        numbers.append(int(line))

if len(numbers) < 3:
    print('Ошибка. В файле менее чем 3 числа!')
else:
    print('1 -', numbers[0])
    print('2 -', numbers[1])
    print('3 -', numbers[-2])
    print('4 -', numbers[-1])
