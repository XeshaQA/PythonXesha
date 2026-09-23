squares = []

with open('file_1.txt', 'r') as f_in:
    for line in f_in:
        clean_line = line.strip()
        if clean_line != '':
            number = float(clean_line)
            square = number ** 2
            squares.append(square)
with open('squares.txt', 'w') as f_out:
    for sq in squares:
        f_out.write(f'{sq}\n')

print('Все числа заменены на квадраты')