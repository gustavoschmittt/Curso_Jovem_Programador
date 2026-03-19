nome = input('Digite o nome do aluno: ')
idade = int(input('Digite a idade do aluno: '))
aluno = {'nome': nome, 'idade': idade}
print(aluno)
print('O nome do aluno é',aluno['nome'])
print("A idade do aluno é", aluno['idade'])
print(type(aluno))

nota = float(input("Digite a nota do aluno: "))
aluno['nota'] = nota
print(aluno)