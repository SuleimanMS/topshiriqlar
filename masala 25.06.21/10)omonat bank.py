while True :
    n = int(input('\nOmonat summasini kiriting (kamida 100 $): '))
    foiz = 22
    oy = 3
    b = 0
    a = (n/100)*foiz 
    if n < 100 :
        print('Xatolik')
    else :
        for x in range(1,oy+1,1) :
            b = b + a 
        print(f'Jami: {b+n}',end='\n')
        print(f'Foyda: {b}')
