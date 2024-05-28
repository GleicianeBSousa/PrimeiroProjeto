'''
    Crie um programa que leia duas notas de um aluno e calcule sua média,
    mostrando uma mensagem no final, de acordo com a média atingida:

        media abaixo de 5.0:
            reprovado

        media entre 5.0 e 6.9:
            recuperação
        
        media 7.0 ou superior:
            aprovado
'''
#Rodrigo
primeira_nota = float(input("Digite a Primeira Nota. "))
segunda_nota = float(input("Digite a Segunda Nota. "))
resultado_da_media = (primeira_nota + segunda_nota)/2

if resultado_da_media <= 5.0:
    print(f"SUA MÉDIA É \033[1;4;41m{resultado_da_media}\033[m VOCÊ ESTÁ \033[1;4;41mREPROVADO\033[m")


elif resultado_da_media <= 6.9:
    print(f"SUA MÉDIA É \033[1;4;43m{resultado_da_media}\033[m VOCÊ ESTÁ \033[1;4;43mRECUPERAÇÃO\033[m")

elif resultado_da_media >= 7.0:

    print(f"SUA MÉDIA É \033[1;4;42m{resultado_da_media}\033[m VOCÊ ESTÁ \033[1;4;42mAPROVADO\033[m")

#Alisson
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) /2
if media < 5.0:
    print('{} \033[1;31m REPROVADO\033[m'.format(media))
elif media  <= 6.9:
     print('{} \033[1;33mRECUPERAÇÃO\033[m'.format(media))
elif media >= 7.0:
    print('{} \033[1;32mAPROVADO\033[m'.format(media))