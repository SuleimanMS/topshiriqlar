print('Soat 12:00')
print('Daqiqani kiriting: ')
a = 12
b = 0
n = int(input('--> '))
c = (n//60)+ a
d = (n%60) + b
if n < 10 :
    print(a,end=':0')
    print(n)
elif (n%60) == 0 :
    print(c,end=':0')
    print(b)    
elif (n/60) > 1 : 
    print(c,end=':')
    print(d)
elif (n/60) < 1 :
    print(c,end=':')
    print(d)
