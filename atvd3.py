i = int(input('Digite sua idade: '))

if (i <= 11):
    print('Você é criança')
elif (i > 11) and (i <= 17):
    print('Você é adolescente!')
elif (i > 17) and (i <= 59):
    print('Você é adulto!')
else:
    print('Você é idoso!')
    