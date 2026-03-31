num = int(input('Digite um número: '))

if (num < 0):
    res = ('negativo!')
elif (num > 0): 
    res = 'positivo!'
else: 
    res = 'zero!'

print(f'O número {num} é {res}')
