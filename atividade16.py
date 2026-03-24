not1 = float(input('Digite a 1° nota: '))
not2 = float(input('Digite a 2° nota: '))
not3 = float(input('Digite a 3° nota: '))
notas = (not1, not2, not3)
media = sum(notas)/len(notas)

print('As notas são:', notas)
print(f'A média das notas são: {media:.1f}')