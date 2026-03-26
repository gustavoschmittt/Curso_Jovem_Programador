inv = []
while True:
   item = input('Escreva o item encontrado: ')
   if item.lower() == 'sair':
        print('Encerrando')
        break
   else:
        inv.append(item)

inv.sort()
print(f'A lista é: {inv}')
print(f'A quantidade coletada de itens foi: {len(inv)}')

