'''
    Faça um programa que leia uma frase qualquer e mostre:
    Quantas vezes aparece a letra "a"
    Em que posição ela aparece a primeira vez
    Em que posição ela aparece a última vez
'''

'''texto='Bom programador? ler e interpretar textos aprender conceitos, não decorar comandos e fazer muitos exercícios'

#contar a quantidade de vezes que aparece a string 'os' no texto
conta = texto.count(subs)
print('quantidade de os = ', conta)
'''

frase = str(input('Digite sua frase preferida: '))
#letra_frase = frase.split()
subs = 'a'
conta = frase.count(subs)
print('A quantidade que a letra a aparece na frase é = ', conta)