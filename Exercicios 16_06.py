#Exercício 1:
#Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro
# def teste():
#     try:
#      n = int(input('Digite um valor inteiro'))
#      print(n)
#     except TypeError as erro:
#      print(erro)  
#     except IndexError as erro:
#      print(erro)
#     else:
#      print('Pode ser um número inteiro') 
#     finally:
#      print('Fim do carregamento')
#     while True:
#       teste()    

#correção prof exercicio 1
# def teste():
#     try:
#         numero = int(input('Numero: '))
#         print(numero)
#     except TypeError as erro:
#         print(erro) 
#     except ValueError  as erro:
#         print(erro)         
#     else:
#         print('Erro não identificado')
#     finally:
#         print('Fim de carregamento... ')    
# teste()


# div()


#Exercício 2:
#Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.
# def teste():
#  try:
#   n = int(input('Digite um valor inteiro'))
#   n2 = int(input('Digite um valor inteiro'))
#   div = n/n2
#   print(div)  
#  except ZeroDivisionError:
#   print("A divisão não ser por zero")  


# while True:
#       teste()    


#correção prof 3xercicio 2
# def div():
#   try:  
#     n1  =  int(input('Numero 1:'))
#     n2  =  int(input('Numero 1:'))
#     d = n1 / n2
#   except ZeroDivisionError as erro:
#     print('Erro',erro)
#   except ValueError as erro:
#     print(erro)
# #   else:
# #     print('Erro não identificado') 


#   finally:
#    print('fim de carregamento')


# div()

# #Exercício 3:
# #Crie uma função que aceite uma lista e um índice como entrada e retorne o parameter elemento naquele índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).
def teste():
    l=[1,2,3,4,5]

#correção prof exercicio 3:

# def ativida3():
#    try: 
#     lista = [1,2,3]
#     indice = int(input('indice: '))
#     lista[indice]
#    except IndexError as erro:
#      print(erro)
#    except ValueError as erro:
#      print(erro)
#    else:
#      print(lista[indice])   
#    finally:
#      print('Fim de carregamento...')  


# ativida3()     
# # l = [1,2,3]
# # print(l[5])

#Resumo: 

# estruturas de dados
# variáveis  - listas []-  tuplas ()  
# conjuntos{} -  dicinario {chave: valor}


# nome  =  
# estruturas de fluxo de controle


# if elif else - escolhas
# while for  - loops
# try and except - tratar possiveis erros
    
# nome <condição>



# funções def nome(): momento esta sendo criando
# nome() -  chamando para funcionar
# print() input() 