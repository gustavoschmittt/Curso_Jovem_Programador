notas = []

while True: 
    nota = float(input('Digite uma nota: '))
    if (nota < 0):
        print('Encerrando')
        break
    else:
        notas.append(nota)   

media = sum(notas)/len(notas)
if (media >= 7):
    situacao = ('situação: Aprovado!')
else:
    situacao = ('situação: Recuperação!')  

print(f'As notas foram: {notas}')
print(f'A sua média foi: {media:.1f}, com a {situacao}')
