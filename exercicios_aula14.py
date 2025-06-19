# #Verificando se o número é par ou ímpar
# n=int (input())
# case (n%2=0):
# print("é um número par")
# case _:
# print("é um número ímpar")

#2: Verificando se um número é positivo, negativo ou zero
n=int(input())
match n:
  case 0:
    print("é positivo")
  case 1:
    print("é negativo")
  case _:
    print("é zero")