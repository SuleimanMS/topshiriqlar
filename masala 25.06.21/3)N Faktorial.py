while True :
    n = int(input('\nNatural son kiriting:\n---> '))
    if n <= 0 :
        print('Faqat natural son kiriting!')
    else :
        a = 1 
        for x in range(1,n+1,1):
            a = a*x
        print(a)
