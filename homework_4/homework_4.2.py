with open('file_1.txt', 'r') as f_in,\
    open('even.txt', 'w') as f_even, \
    open('odd.txt', 'w') as f_odd:
    for line in f_in:
        clean_line = line.strip()
        if clean_line != '':
            number = int(clean_line)
        if number % 2 == 0:
            f_even.write(str(number) + '\n')
        else:
            f_odd.write(str(number) + '\n')

    f_in.close()
    f_even.close()
    f_odd.close()

    print('Выполнено')