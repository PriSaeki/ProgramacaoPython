# a=3
# b=4
# def soma(a,b):
#     c=a+b
#     print(c)

# def subtracao(a,b):
#     c=a-b
#     print(c)
#     return c


# resultado=subtracao(a,b)
# print(resultado)

#Exercício de função
# 1 - Verificação de emails válidos
#crie uma função que receba um emaile verifique se ele contém @ e .com. Caso contrário, diga "E-mail inválido"

# def validar_email(email):
#     if "@" in email and ".com" in email:
#         return "E-mail válido"
#     else:
#         return "E-mail inválido"
    
# 2 - Sistema de Ponto
#use input() para receber os horários de entrada e saída. Calcule as horas trabalhadas e diga se bateu a carga horária mínima (8h).

horario_de_entrada=float(input("Qual horário de entrada?"))
horario_de_saida=float(input("Qual o horário de saída?"))

def horas_trabalhadas():
    horas_trabalhadas=horario_de_saida-horario_de_entrada
    print(horas_trabalhadas)


horas_trabalhadas()

    
