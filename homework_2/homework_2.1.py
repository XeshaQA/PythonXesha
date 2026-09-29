for x in range (1, 31):
    if x % 3 == 0 and x % 5 == 0:
        print('BugTest')
    elif x % 3 == 0:
        print('Bug')
    elif x % 5 == 0:
        print ('Test')

    else:
        print(x)