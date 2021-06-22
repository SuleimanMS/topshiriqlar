print('Pirog sonini kiriting: ')
n = int(input('--> '))
rubl = 10
kopek = 15
if (n*kopek) < 100 :
    print(n*rubl,end='.')
    print(n*kopek)
elif (n*kopek) > 100 :
    a=(n*kopek)//100
    b=(n*kopek)%100
print((n*rubl)+a,end='.')
print(b)


