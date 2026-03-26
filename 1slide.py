temp = float(input('Qual a temperatura atual? '))

if (temp < 10):
    print("A temperatura está muito frio!")
elif (temp >= 10) and (temp <= 24):
    print('A temperatura está agradável!')
elif (temp >= 25) and (temp <= 30):
    print('A temperatura está quente!')
else:
    print('A temperatura está muito quente!')
    
