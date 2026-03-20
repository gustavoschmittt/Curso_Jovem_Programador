nome = input("Digite o nome do produto: ")
preco = float(input('Qual o preço do produto: '))
desconto =  (preco*10)/100
produto = {'nome': nome, 'preco': preco, 'desconto': desconto}
print(produto)

produto.pop('desconto',2)
print(produto)