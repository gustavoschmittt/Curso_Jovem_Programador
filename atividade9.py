nome = input("Digite o nome do produto: ")
preco = float(input('Qual o preço do produto: '))
quantidade = int(input('Qual a quantidade do produto: '))
produto = {'nome': nome, 'preco': preco, 'quantidade': quantidade}
aumento = (preco*5)/100 + preco
nvpreco = aumento
nvquantidade = quantidade + 2
produto['preco'] = nvpreco
produto['quantidade'] = nvquantidade
total = nvpreco * nvquantidade
print(produto)
print('O valor total é: ',total)