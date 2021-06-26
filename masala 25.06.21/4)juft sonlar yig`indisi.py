while True :
    n = int(input('\nNatural son kiriting:\n---> '))
    if n <= 0 :
        print('Natural son kiriting!')
    else :
        a = 0
        for x in range(2,n+1,2) :
            a = a+x
        print(a)
