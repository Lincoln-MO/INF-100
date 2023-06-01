ano1=int(input('Digite o ano inicial (1582 a 2499): '))
ano2=int(input('Digite o ano final   (1582 a 2499): '))
while ( ano1 < 1582 or ano1 > 2499 ) or ( ano2 < 1582 or ano2 > 2499):
    ano1=int(input('Digite o ano inicial (1582 a 2499): '))
    ano2=int(input('Digite o ano final   (1582 a 2499): '))
print('Ano      Data da Páscoa')
print('-----------------------')
ano=ano1
while ano1 <= ano <= ano2 :
    if ano <= 1699:
        x= 22
        y= 2
    elif ano <= 1799:
        x= 23
        y= 3
    elif ano <= 1899:
        x= 23
        y= 4
    elif ano <= 2099:
        x= 24
        y= 5
    elif ano <= 2199:
        x= 24
        y= 6
    elif ano <= 2299:
        x= 25
        y= 0
    elif ano <= 2399:
        x= 26
        y= 1
    else:
        x= 26
        y= 1
    a= ano % 19
    b= ano % 4
    c= ano % 7
    d= (19*a+x)% 30
    e= (2*b+4*c+6*d+y)%7
    p=(22+d+e)
    if p <= 31:
        print('%d      %d de março' % (ano,p))
    else:
        p1=(d+e-9)
        if p1 <= 25:
               print('%d      %d de abril' % (ano,p1))
        else:
            p2=(p1-7)
            print('%d      %d de abril' % (ano,p2))
    ano= ano + 1
    
              


        

            
