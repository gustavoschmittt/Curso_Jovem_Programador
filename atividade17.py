num1 = int(input('Digite um numero:'))
num2 = int(input('Digite um numero:'))
num3 = int(input('Digite um numero:'))
num4 = int(input('Digite um numero:'))
numeros = (num1, num2, num3, num4)
lista = [numeros]

print('A tupla ordenada fica:', sorted(lista))
print(type(sorted(lista)))
