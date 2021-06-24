while True :
    n = int(input('\nYoshingizni kiriting: '))
    if n < 0 and n >= 150 :
        print('Xatolik') 
    else : 
        if n >= 0 and n <= 5 :
            print('Chaqaloq')
        elif n >= 6 and n <= 12 :
            print('Bola')
        elif n >= 13 and n <= 19 :
            print('O`spirin')
        elif n >= 20 and n <= 50 :
            print('Yoshroq')
        elif n >= 50 and n <= 100 :
            print('Keksa')
        else :
            print('Asr Odami') 
