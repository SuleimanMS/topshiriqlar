while True :
    a = int(input('\nOy tartib raqamini kiriting: '))
    b = int(input('Kunni kiriting: ')) 
    kun = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 30, 30, 31,0,0,0,0,0,0,0,0,0,0,0,0]
    if a <= 0 or a >= 13:
        print('Xatolik') 
    else :
        qoldi=(kun[a]-b)+(kun[a+1]+kun[a+2]+kun[a+3]+kun[a+4]+kun[a+5]+kun[a+6]+kun[a+7]+kun[a+8]+kun[a+9]+kun[a+10]+kun[a+11])
        print(qoldi)
