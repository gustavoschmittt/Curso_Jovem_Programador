nota = float(input('Digite uma nota: '))

if (nota < 5 ):
    situacao = ('Reprovada')
elif (nota >= 5) and (nota <  7):
    situacao = 'Em recuperação'
elif (nota >= 7) and ( nota < 9): 
    situacao = 'Aprovada'
else:
    situacao = 'Aprovada com excelência'

print(f'Sua nota foi {nota:.1f} e você está: {situacao} ')
