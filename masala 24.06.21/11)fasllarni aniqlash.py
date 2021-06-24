while True :
    n = int(input('\nOy tartib raqamini kiriting:\n---> '))
    if n <= 0 or n >=13 :
        print('Xatolik!')
    else :
        if n >= 3 and n <= 5 :
            print('Bahor')
        elif n >=6 and n <= 8 :
            print('Yoz')
        elif n >= 9 and n <= 11 :
            print('Kuz')
        else :
            print('Qish')