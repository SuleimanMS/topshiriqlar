while True :
    n = int(input('\nOy tartib raqamini kiriting:\n---> '))
    kun = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 30, 30, 31]
    if n <= 0 :
        print('Xatolik') 
    else :
        print(kun[n])
