while True : 
    a = int(input('\n3ta son kiriting:\na = '))
    b = int(input('b = '))
    c = int(input('c = '))
    if a == b and a == c :
        print(3)
    elif a == b or a == c :
        print(2)
    else :
        print(0)
