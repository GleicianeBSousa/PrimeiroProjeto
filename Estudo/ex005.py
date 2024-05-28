lista_aluno = []
while len(lista_aluno) <3:
    aluno = input('Digite o nome do aluno: ')
    lista_aluno.append(aluno)
print(lista_aluno)
if 'carina' in lista_aluno:
    print('Tem carina')
else:
    print('Não tem carina ')
