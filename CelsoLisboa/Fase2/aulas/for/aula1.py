lista = ["carbauba", "perola"]
tupla = (1,2,3,4,5, lista)
dicio = {
    "item" : tupla
}
for tempo in range(1,6):
    nome = str(input("Digite um item: "))
    add = lista.append(nome)
print(lista)
print(tupla)
print(dicio)