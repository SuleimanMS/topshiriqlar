while True :
    A = int(input('\nIkkita son kiriting:\nA = '))
    B = int(input('B = '))
    if A >= 0 and B >= 0 :
        if A >= B :
            for x in range(B,A,1) :
                print(x,end=", ")
        else :
            for x in range(A,B,1) :
                print(x,end=", ")
    elif A <= 0 and B <= 0 :
        if A >= B :
            for x in range(B,A,1) :
                print(x,end=", ")
        else :
            for x in range(A,B,1) :
                print(x,end=", ")
    elif A <= 0 or B <= 0 :
        if A >= B :
            for x in range(B,A,1) :
                print(x,end=", ")
        else :
            for x in range(A,B,1) :
                print(x,end=", ")                
