n1 = int(input('Escreva um número: '))
n2 = int(input('Escreva um número: '))
op = (input('Qual operação quer usar:  (+, -, /, *) '))

if (op == '+'):
    res = n1 + n2
    print(f'{n1} + {n2} = {res}')
elif (op == '-'):
    res = n1 - n2
    print(f'{n1} - {n2} = {res}')
elif (op == '/'):
    res = n1 / n2
    print(f'{n1} / {n2} = {res}')   
elif (op == '*'):
    res = n1 * n2
    print(f'{n1} * {n2} = {res}')
else:
    print('ERRO')