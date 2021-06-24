while True :
    a = int(input('\n2 ta son kiriting:\na = '))
    b = int(input('b = '))
    if a == 0 and b == 0 :
        print('Toq sonlar emas!')
    elif a%2 != 0 and b%2 != 0 :
        print('Toq sonlar')
    else :
        print('Toq sonlar emas!')
