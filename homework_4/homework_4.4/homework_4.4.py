with open('file_switch_1.txt', 'r') as f1:
    data1 =f1.read()

with open('file_switch_2.txt', 'r') as f2:
    data2 = f2.read()

with open('file_switch_1.txt', 'w') as f1:
    f1.write(data2)

with open('file_switch_2.txt', 'w') as f2:
    f2.write(data1)

print('Смена содержимого файлов местами прошла успешно')