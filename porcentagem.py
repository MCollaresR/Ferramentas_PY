x=0
while x == 0:
    print('a/b * c = d')
    # variavel = input('variavel que deseja: (a, b, c, d)')
    # a = float(input('a: '))
    b = float(100)
    c = float(input('Valor total: '))
    d = float(input('valor da parte: '))
    a = b*d/c
    
    print('porcentagem de da parte sobre o valor total: {}%'.format(a))
    
    rsp = input('1 para repetir: ')
    if rsp != '1':
        x = x+1
        print('x: ',x)
        print('fim do programa!')