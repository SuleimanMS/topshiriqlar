print('Sekundni kiriting: ')
n = int(input('--> '))
soat = 00
minut = 00
sek = 00
if n < 10 :
    print(soat,end=':0')
    print(minut,end=':0')
    print(n)
elif n >= 10 and n < 60 :
    print(soat,end=':0')
    print(minut,end=':')
    print(n)

   
