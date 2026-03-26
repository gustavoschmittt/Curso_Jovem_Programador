peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura **2)

if (imc < 18.5): 
    categoria = 'Magreza'
elif (imc < 25): 
    categoria = 'Normal'
elif (imc < 30):
    categoria = 'Sobrepeso'
else:
    categoria = 'Obesidade'

print(f'IMC = {imc:.2f} - {categoria}')
