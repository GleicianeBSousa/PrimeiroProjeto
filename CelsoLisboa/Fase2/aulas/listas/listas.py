# criar uma lista []
# criar um dicionario {}
# criar tuplas ()
# metodo append que é variavel da lista.append(nome do input) é para adicionar
# metodo remove é para remover da mesma forma que o appende(), remove()

lista2 = []
lista = ['arroz', 'feijao', 'batata', 'bife', 'refrigerante', 'tomate']
novo = str(input('Digite um item há lista: '))
novo2 = str(input('Digite outro nome na lista: '))
add = lista.append(novo)
add2 = lista.append(novo2)
add3 = lista.append('cerveja')
print(lista)
remo = str(input('Remova um intem da lista: '))
remover = lista.remove(remo)
print(lista)
