agenda = {'Ana':'1111-1111', 'Bruno':'2222-2222'}
nome = input('Digite seu nome: ')
cont = input('Digite seu numero de contato:')
agenda[nome] = cont
print('A lista atualizada é: ',agenda)

agenda['Ana'] = '4444-4444'
print(agenda)

agenda.pop('Ana')
print(agenda)
