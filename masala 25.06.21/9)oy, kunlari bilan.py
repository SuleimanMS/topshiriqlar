while True :
    n = int(input('\nOy tartib raqamini kiriting:\n---> '))
    oy = ['Yanvar','Fevral','Mart','Aprel','May','Iyun','Iyul','Avgust','Sentyabr','Oktyabr','Noyabr','Dekabr']
    if n <  1 or n > 12 :
        print('Xatolik!')
    else :
        print(f'\n{oy[n-1]}',end=': ')
        if n == 1 or n == 3 or n == 5 or n == 7 or n == 8 or n == 10 or n == 12 :
            for x in range(1,32,1) :
                print(x,end=', ')
        elif n == 4 or n == 6 or n == 9 or n == 10 or n == 11 :
            for y in range(1,31,1) :
                print(y,end=', ')
        else :
            for z in range(1,29,1) :
                print(z,end=', ')
                
    
