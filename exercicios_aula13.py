
# #exercio 01
# with open('novo_diretorio', 'w') as novo_arquivo:
#     os.mkdir('novo_arquivo')
    
# with open('exemplo.txt', 'r') as arquivo:
#     conteúdo = arquivo.read()
#     print(conteúdo)


# #exercio2
# import os
# with os.scandir('c:/Users/aluno/Desktop/aula12/') as entrada:
#       for arquivo in entrada:
#          print(f'Diretório encontrado: {arquivo.name}')


# #exercicio3
# import os
# os.rename('exemplo.txt', 'test5.txt')

# #exercicio4
# import os
# with os.scandir('meu_diretorio') as entrada:
#     for arquivo in entrada:
#         if arquivo.is_file():
#             print(f'Arquivo encontrado: {arquivo.name}')

# #exercicio5
# import shutil
# shutil.copytree('original', 'nome da copia')
# # serve para pastas -> diretórios

# #exercicio6
# import shutil
# shutil.rmtree('c:/Users/aluno/Desktop/aula12/')
