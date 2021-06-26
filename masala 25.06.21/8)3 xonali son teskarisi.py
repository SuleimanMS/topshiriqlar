while True :
    n = int(input('\nNatural son kiriting:\n---> '))
    if n >= 100 and n < 1000 :
        a = (n%10)*100
        b = ((n//10)%10)*10
        c = n//100
        print(a + b + c)
    else :
        print('3 xonali son kiriting!')

