print('Uch xonali raqam kiritng: ')
n = int(input('--> '))
if n >= 100 and n < 1000 : 
    uch = n%10 
    ikki = (n//10)%10
    bir = n//100
    print(uch + ikki + bir)
else : 
    print('Faqat uch xonali son kiriting')
