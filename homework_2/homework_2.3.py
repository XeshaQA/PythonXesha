user = 1

while user <= 20:
    if user == 5 or user == 10 or user == 15:
        print('-')
        user += 1
        continue

    if user == 19:
        break
    else:
        print (user)

    user += 1