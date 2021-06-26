while True :
    n = int(input('\nNatural son kiriting\n---> '))
    if n <= 0 :
        print('Natural son kiriting!')
    else :
        a = 0
        for x in range(1,n+1,1) :
            a = a+x 
            b = a/n
        print(b)
